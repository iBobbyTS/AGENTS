# 技能安装与宿主配置

唯一技能安装入口是 `scripts/install.py`，需要 Python 3.11+。从仓库根目录运行；默认只预览，不写入任何目标文件。

```sh
python3 scripts/install.py --target codex
python3 scripts/install.py --target zcode --home "/absolute/custom home"
```

确认预览后加 `--apply`。更新已有安装时加 `--replace`：先备份将被替换的精确目标，再安装新版本。备份保存在宿主 home 的 `sfd-backups/`，其中 `manifest.json` 记录恢复位置。默认 home 优先使用 `CODEX_HOME` / `ZCODE_HOME`，否则为 `~/.codex` / `~/.zcode`；`--home` 指宿主目录，不是 skills 目录。`--host` 是 `--target` 的别名。

```sh
python3 scripts/install.py --target codex --apply --replace
```

## 安装范围

- 安装仓库 `skills/` 下的完整技能目录，包括 SFD、code-review、三个 QC 技能和原有其他技能。QC 三个技能必须保持同级，共享 general-audit 的知识库。
- 按宿主安装 `agents/codex/` 或 `agents/zcode/` 的原生角色，将对应 SFD dispatch 文档嵌入安装后的 model-routing.md，并写入 installation.json。不要只复制 SFD 的 SKILL.md。
- 不修改宿主全局配置。只有显式传入 `--include-agents-md` 才安装仓库根 AGENTS.md；覆盖已有文件仍需 `--replace`。
- 不执行 git pull；需要更新时先自行拉取、审阅，再运行安装器。旧 `sync_codex_config.py` 已由本入口取代。
- 不改动目标目录中不属于本仓库的其他技能与原生角色。目标或源路径出现符号链接时拒绝安装，避免越界写入。
- 已安装的旧 code-audit 会阻止完整安装；确认使用 `--replace` 后先备份，再从活动 skills 目录移除。项目内历史审计报告不受影响。
- 仅需更新 code-review 时可用 `--only code-review`；此模式不安装 SFD、QC、原生角色或 external profiles，也不清理旧 code-audit。
- 若要清理旧 SFD Codex 原生角色，额外使用 `--retire-legacy-agents`，且必须完整安装并带 `--target codex --replace`。仅清理脚本列出的旧角色名称，清理前备份。

## External profiles

安装器保留 SFD 的宿主专用和共享 spawn profiles。默认从 macOS 的 `~/Library/Application Support/external-subagent`，或其他系统的 `$XDG_DATA_HOME/external-subagent`（未设置时 `~/.local/share/external-subagent`）判断数据目录。目录不存在时警告并跳过 profiles；可用 `--profiles-dir` 明确指定目标目录。

已有内容不同的同名 profile 需要 `--replace` 才能备份替换。清理过期 `sfd-*.json` 时按两个宿主的联合清单判断，保留另一宿主仍使用的 profile 和非 SFD 文件。技能、角色及本次变更的 profiles 一起暂存，普通发布错误会回滚；不支持同时对同一 home 运行多个安装器，也不承诺断电恢复。

安装不配置或启动 external-subagent，不接入模型 API，不证明实时角色发现或模型身份正确。使用前仍需在实际宿主验证角色发现、AGENTS 隔离、model/effort 与外部运行能力。

## QC 使用与提醒

三个 QC 入口：quality-steward 做轻量分流，general-audit 做独立深度审计，deployment-preflight 做用户触发的发布前检查。示例：

- “用 quality-steward 看现在是否值得审计。”
- “用 general-audit 做一次 routine 审计。”
- “准备交付此候选，用 deployment-preflight 检查，不部署。”

安装不会登记仓库、运行扫描、安装定时器、修改 hook 或授权审计/部署。模型、调度与登记文件要求见 [QC 宿主配置](QUALITY-HOST-CONFIG.zh-CN.md)，该文档不复制进宿主技能目录。现有 Git 提醒仍按 [Git hook 文档](../git-hook.md) 单独选择启用。
