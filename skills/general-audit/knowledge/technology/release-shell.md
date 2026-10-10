# Scripts, file selection and release environment

**Select only:** shell/platform behavior, working-directory dependence or built-package contents decides a concrete audit question. Use actual supported shells and OSes; do not turn this into basic syntax instruction.

**Hypothesis:** a scan/build command returns success while processing a narrower population than intended, or a package works only because the checkout supplies undeclared files/environment.

**Distinguish:** inspect expanded arguments, include/exclude rules, working directory, symlinks, case/line-ending assumptions, environment inheritance and emitted artifact contents at the implicated seam. In a disposable fixture, compare selected filenames with a known expected set. Include a filename that could accidentally match a shell wildcard when glob filters are intended to remain literal. Record tool version, command and actual population, not just exit code.

A Trail of Bits issue reports unquoted shell expansion turning include patterns into local filenames, silently dropping intended scan coverage. Treat it as a reported mechanism, not a universal verdict on that tool. ([reported issue](https://github.com/trailofbits/skills/issues/297))

For a published package, inspect its real manifest/exports/binaries and, where authorized, consume the built artifact outside the source tree. Check supported path/permission handling; do not invent unsupported platform requirements.

**Counterevidence:** explicit excludes can be intentional and safe; absent files can be supplied by a documented consumer contract. An observed successful source-tree import is simply insufficient to decide artifact completeness. Prefer repairing argument transport or the package boundary over adding another global scan gate.

Related release trust: [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use). No external process, download or package installation is automatically authorized by this card.
