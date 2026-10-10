#!/usr/bin/env python3
"""Local external-advisor request pack: worktree + Git, no model, upload, reset or checkout.

Detected secret-like or uninspected content is excluded and recorded in
PACKAGE-EXCLUSIONS.json. Filtering is best effort; sharing still needs human review.
Optional CLI bounds (--exclude/--include/--include-git/--include-agent-work) only add or
re-add content; they never bypass the secret filter.
Layout: .agent-work/advisor/{YYYYMMDD-HHMM_feature-id}/request/ (note + zip + receipts)
with a sibling response/ directory for the returned advisor result.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import time
import zipfile
from pathlib import Path

SECRET_NAMES={'.env','.env.local','.env.production','id_rsa','id_ed25519','credentials.json','secrets.json'}
SECRET_PATTERNS=[re.compile(rb'-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----'),re.compile(rb'(?i)(?:api[_-]?key|token|secret|password)\s*[:=]\s*["\']?[A-Za-z0-9_\-]{20,}'),re.compile(rb'https?://[^\s/@:]+:[^\s/@]+@')]
EXCLUDE_PARTS={'.venv','venv','node_modules','__pycache__','.pytest_cache','.mypy_cache','.ruff_cache','target','dist','build','.next','.svelte-kit'}
REQUEST_ID=re.compile(r'^\d{8}-\d{4}_[a-z0-9][a-z0-9-]{0,63}$')
ID=re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.-]{0,95}$')
SCAN_CHUNK=1024*1024
SCAN_OVERLAP=65536
BIG_FILE_LIMIT=2*1024*1024

def sensitive_name(name):
 p=Path(name)
 return p.name in SECRET_NAMES or p.name.startswith('.env.') or p.suffix.lower() in {'.pem','.p12','.pfx','.key'}

def excluded_content(data):
 return any(rx.search(data) for rx in SECRET_PATTERNS)

def stream_excluded(handle,size):
 # Full-content secret scan of any size; None marks a short read (uninspected).
 tail=b'';left=size
 while left>0:
  chunk=handle.read(min(SCAN_CHUNK,left))
  if not chunk:return None
  left-=len(chunk);window=tail+chunk
  if any(rx.search(window) for rx in SECRET_PATTERNS):return True
  tail=window[-SCAN_OVERLAP:]
 return False

def path_excluded(p,size):
 with p.open('rb') as source:return stream_excluded(source,size)

def agent_path(value):
 p=Path(value)
 if not value or p.is_absolute() or '..' in p.parts or p.as_posix()=='.':raise ValueError('agent include/exclude must be a relative in-repo path: '+str(value))
 return p.as_posix()

def human_size(size):
 if size<1024:return f'{size} Bytes'
 if size<1024*1024:return f'{size/1024:.2f} KB'
 return f'{size/(1024*1024):.2f} MB'

def agent_instruction(total):
 return ('AGENT_INSTRUCTION: more than 50 big files archived, verify including and excluding policy' if total>50
         else f"AGENT_INSTRUCTION: {total} big files archived, verify if they're necessary")

def history_exportable(repo):
 # Inspect decompressed reachable objects; raw .git also contains unreferenced objects,
 # local credentials and hooks, so it is never a sharing artifact.
 objects=git(repo,'rev-list','--objects','--all','HEAD').splitlines()
 with subprocess.Popen(['git','-C',str(repo),'cat-file','--batch'],stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,stderr=subprocess.DEVNULL) as proc:
  try:
   for row in objects:
    oid,_,name=row.partition(b' ')
    if name and sensitive_name(os.fsdecode(name)):return False
    proc.stdin.write(oid+b'\n');proc.stdin.flush()
    header=proc.stdout.readline().split()
    if len(header)!=3 or not header[2].isdigit():return False
    size=int(header[2])
    if header[1]==b'blob':
     # Stream any object size; a short read is uninspected and fails the export.
     if stream_excluded(proc.stdout,size) or proc.stdout.read(1)!=b'\n':return False
    else:
     data=proc.stdout.read(size)
     if len(data)!=size or proc.stdout.read(1)!=b'\n' or excluded_content(data):return False
     if header[1]==b'tree':
      tree=data
      while tree:
       entry,_,rest=tree.partition(b'\0')
       if sensitive_name(os.fsdecode(entry.partition(b' ')[2])):return False
       tree=rest[len(oid)//2:]
   return True
  finally:
   proc.stdin.close()
   if proc.poll() is None:proc.terminate()

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def git(repo,*args,check=True):
 return subprocess.run(['git','-C',str(repo),*args],check=check,capture_output=True).stdout

def worktree_status(repo):
 # The advisor request tree lives inside the repo; its own packaging output must not look like user-work changes.
 return [x for x in git(repo,'status','--porcelain=v1','-z','--untracked-files=all').decode().split('\0')
         if x and not x[3:].startswith('.agent-work/advisor')]

def collect(root,arc,tracked=(),exclusions=None,metadata=False,skip_prefixes=(),include_parts=(),include_git=False):
 exclusions=exclusions if exclusions is not None else []
 result=[]
 for base,dirs,names in os.walk(root,followlinks=False):
  b=Path(base)
  for n in list(dirs):
   p=b/n;rel=p.relative_to(root).as_posix()
   if n=='.git' and not include_git:
    exclusions.append(str(Path(arc)/rel)+' (raw Git metadata)');dirs.remove(n);continue
   if p.is_symlink():result.append((p,str(Path(arc)/rel)));dirs.remove(n);continue
   if any(rel==s or rel.startswith(s+'/') for s in skip_prefixes):
    exclusions.append(str(Path(arc)/rel)+' (excluded export tree)');dirs.remove(n);continue
   in_git=metadata or rel=='.git' or rel.startswith('.git/')
   if not in_git and n in EXCLUDE_PARTS and not any(t==rel or t.startswith(rel+'/') for t in tracked) \
      and not any(rel==s or rel.startswith(s+'/') for s in include_parts):
    exclusions.append(str(Path(arc)/rel));dirs.remove(n)
  for n in names:
   p=b/n;rel=p.relative_to(root).as_posix()
   if n=='.git' and not include_git:
    exclusions.append(str(Path(arc)/rel)+' (raw Git metadata)');continue
   if any(rel==s or rel.startswith(s+'/') for s in skip_prefixes):
    exclusions.append(str(Path(arc)/rel)+' (excluded export tree)');continue
   if p.is_symlink() or p.is_file():result.append((p,str(Path(arc)/rel)))
   else:exclusions.append(str(Path(arc)/rel)+' (non-regular)')
 return result

def build(repo,request,trigger,include=(),exclude=(),include_git=False,include_agent_work=False):
 repo=repo.resolve()
 if not REQUEST_ID.fullmatch(request) or not ID.fullmatch(trigger):raise ValueError('invalid request/trigger identity')
 includes=tuple(agent_path(x) for x in include);excludes=tuple(agent_path(x) for x in exclude)
 _,feature=request.split('_',1)
 if not all(ID.fullmatch(x) for x in (repo.name,feature)):raise ValueError('invalid export identity')
 if not (repo/'.git').exists():raise ValueError('repository .git directory or linked-worktree file required')
 root=repo/'.agent-work/advisor'/request
 req=root/'request';resp=root/'response'
 if not (req/'ADVISOR-REQUEST.md').is_file():raise ValueError('missing '+str(req/'ADVISOR-REQUEST.md'))
 req.mkdir(parents=True,exist_ok=True);resp.mkdir(parents=True,exist_ok=True)
 head=git(repo,'rev-parse','HEAD').decode().strip()
 refs=git(repo,'show-ref',check=False)
 status=worktree_status(repo)
 tracked=[x for x in git(repo,'ls-files','-z').decode().split('\0') if x]
 exclusions=[]
 # Default red lines are opt-in now: raw .git and .agent-work stay out unless requested;
 # with --include-agent-work only this request's own request/ output directory stays out.
 skip=('.agent-work/advisor/'+request+'/request',) if include_agent_work else ('.agent-work/advisor',)
 skip=skip+excludes
 files=collect(repo,repo.name,tracked,exclusions,skip_prefixes=skip,include_parts=includes,include_git=include_git)
 linked=(repo/'.git').is_file()
 excluded=[]
 target=req/f'{repo.name}-{feature}-{trigger}.zip'
 if target.is_symlink():raise ValueError('request zip path is a symlink')
 manifest=[]
 with tempfile.TemporaryDirectory(prefix='.advisor-',dir=req) as temp:
  temp=Path(temp);bundle=temp/'repository.bundle';archive=temp/'output.zip'
  bundle_ok=history_exportable(repo)
  if bundle_ok:
   git(repo,'bundle','create',str(bundle),'--all','HEAD')
   git(repo,'bundle','verify',str(bundle))
   files.append((bundle,'GIT-METADATA/repository.bundle'))
  else:excluded.append('GIT-METADATA/repository.bundle (sensitive or uninspected history)')
  with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,allowZip64=True) as z:
   for p,arc in files:
    st=p.lstat()
    if stat.S_ISLNK(st.st_mode):
     data=os.readlink(p).encode()
     if sensitive_name(p.name) or excluded_content(data):excluded.append(arc);continue
     info=zipfile.ZipInfo(arc);info.create_system=3;info.external_attr=(stat.S_IFLNK|0o777)<<16
     z.writestr(info,data);manifest.append({'path':arc,'kind':'symlink','size':len(data),'sha256':hashlib.sha256(data).hexdigest()});continue
    # No size limit: every file is fully scanned, then stream-written under the freeze check.
    if p!=bundle and (sensitive_name(p.name) or path_excluded(p,st.st_size) is not False):
     excluded.append(arc);continue
    h=hashlib.sha256();size=0;info=zipfile.ZipInfo.from_file(p,arc);info.compress_type=zipfile.ZIP_DEFLATED
    with p.open('rb') as source,z.open(info,'w',force_zip64=True) as dest:
     for data in iter(lambda:source.read(SCAN_CHUNK),b''):dest.write(data);h.update(data);size+=len(data)
    if p.stat().st_mtime_ns!=st.st_mtime_ns or size!=st.st_size:raise ValueError('source changed during freeze: '+arc)
    manifest.append({'path':arc,'kind':'file','size':size,'sha256':h.hexdigest()})
   for name,args in [('STATUS.txt',('status','--short')),('DIFF.patch',('diff','--binary','HEAD')),('INDEX.patch',('diff','--binary','--cached')),('REFS.txt',('show-ref',)),('SUBMODULES.txt',('submodule','status','--recursive'))]:
    data=git(repo,*args,check=False);arc='GIT-EVIDENCE/'+name
    unsafe_path=False
    if name in {'DIFF.patch','INDEX.patch'}:
     changed=git(repo,'diff','--name-only','-z',*(['--cached'] if name=='INDEX.patch' else ['HEAD'])).split(b'\0')
     unsafe_path=any(sensitive_name(os.fsdecode(p)) or str(Path(repo.name)/os.fsdecode(p)) in excluded for p in changed if p)
    if unsafe_path or excluded_content(data) or b'GIT binary patch' in data:
     excluded.append(arc);continue
    z.writestr(arc,data);manifest.append({'path':arc,'size':len(data),'sha256':hashlib.sha256(data).hexdigest(),'kind':'file'})
   restore=('Read-only archive. If repository.bundle is present: clone it, checkout the frozen HEAD and overlay the archived worktree. '
            'Without a bundle, use the filtered source snapshot; history is unavailable. Raw .git is excluded. '
            'Consult the manifest for omissions. Filtering cannot certify secret-free content; review before sharing. No submodule/LFS download was performed.\n')
   z.writestr('RESTORE.md',restore);manifest.append({'path':'RESTORE.md','kind':'file','size':len(restore.encode()),'sha256':hashlib.sha256(restore.encode()).hexdigest()})
   meta={'schema':'advisor-pack-v2','repo':repo.name,'feature':feature,'trigger':trigger,'request':request,'head':head,'linked_worktree':linked,
    'created_at':time.time(),'files':manifest,'exclusions':sorted(exclusions),'excluded_secret_like':sorted(set(excluded)),
    'agent_includes':list(includes),'agent_excludes':list(excludes),
    'git_bundle_verified':bundle_ok,'automatic_upload':False}
   z.writestr(repo.name+'/ADVISOR-PACK-MANIFEST.json',json.dumps(meta,indent=2))
  if git(repo,'rev-parse','HEAD').decode().strip()!=head or git(repo,'show-ref',check=False)!=refs or worktree_status(repo)!=status:raise ValueError('Git changed during packaging; keep feature paused')
  with zipfile.ZipFile(archive) as z:
   bad=z.testzip()
   if bad:raise ValueError('zip crc failure: '+bad)
  os.replace(archive,target)
 digest=sha(target)
 (req/'PACKAGE-EXCLUSIONS.json').write_text(json.dumps({'status':'FILTERED_REVIEW_REQUIRED','excluded_secret_like':sorted(set(excluded)),'not_included_advisor_tree':sorted(exclusions)},indent=2)+'\n')
 big=sorted((e for e in manifest if e.get('size',0)>BIG_FILE_LIMIT),key=lambda e:e['path'])
 receipt={'path':str(target),'sha256':digest,'file_count':len(manifest),'head':head,'git_bundle_verified':bundle_ok,'request_id':request,
          'response_dir':str(resp),'excluded_secret_like':sorted(set(excluded)),'share_status':'HUMAN_REVIEW_REQUIRED',
          'agent_includes':list(includes),'agent_excludes':list(excludes),
          'big_files':[{'path':e['path'],'size':e['size'],'size_human':human_size(e['size'])} for e in big[:50]],
          'big_files_total':len(big),'agent_instruction':agent_instruction(len(big)),
          'final_zip_size':human_size(target.stat().st_size)}
 (req/'PACKAGE-RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
 return receipt

def main(argv=None):
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--repo',default='.')
 ap.add_argument('--request',required=True,help='directory name YYYYMMDD-HHMM_feature-id under .agent-work/advisor containing request/ADVISOR-REQUEST.md')
 ap.add_argument('--trigger',required=True)
 ap.add_argument('--include',action='append',help='relative untracked build/cache directory to include despite the default exclusion (repeatable)')
 ap.add_argument('--exclude',action='append',help='relative in-repo path prefix to exclude from this export, recorded (repeatable; wins over --include)')
 ap.add_argument('--include-git',action='store_true',help='also archive raw .git metadata; secret filtering still applies')
 ap.add_argument('--include-agent-work',action='store_true',help="also archive .agent-work content; this request's own request/ output directory stays out")
 a=ap.parse_args(argv)
 try:
  receipt=build(Path(a.repo),a.request,a.trigger,include=a.include or (),exclude=a.exclude or (),
                include_git=a.include_git,include_agent_work=a.include_agent_work)
  print(json.dumps(receipt))
  for item in receipt['big_files']:print(f"{item['path']} ({item['size_human']})",file=sys.stderr)
  print(receipt['agent_instruction'],file=sys.stderr)
  print(f"final zip size: {receipt['final_zip_size']}",file=sys.stderr)
  return 0
 except (OSError,ValueError,subprocess.CalledProcessError) as exc:print(str(exc),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
