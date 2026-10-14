# Git Hook 审计提醒方案

这套方案的目标很简单：让所有由 Git 管理、由 AI agent 参与开发的项目，在提交时自动提醒是否需要做一次可维护性审计。

## 设计思想

1. 提醒逻辑放在 Git hook，不放在 agent 自己的判断里。
2. 可执行脚本随仓库版本控制；机器级安装只写入用户自己的 Git 配置。
3. 提醒必须是非阻塞的，只负责输出提示，不影响 commit 成功。
4. 明确的审计标记优先于猜测。最近一次带 `Maintenance-Audit: true` 的提交，是最新审计点。
5. 配置键、脚本名与输出消息统一使用 `agent` 命名空间，不绑定任何具体宿主。

## 配置项

提醒读取两级 `agent.*` 配置，仓库本地优先、全局兜底：

```sh
git config --local  agent.maintainabilityAuditInterval <N>   # 本仓库间隔，覆盖全局
git config --global agent.maintainabilityAuditInterval <N>   # 全局默认间隔
git config --local  agent.maintainabilityAuditBaseline <HEAD_SHA>   # 可选基线
```

推荐的全局默认是 100：所有未单独配置的仓库按 100 次提交提醒一次；某个项目想更勤或更松，只需在仓库内改本地值（例如 50 或 200），不影响其他仓库。

- `agent.maintainabilityAuditInterval` 是审计间隔，必须是数字；≤0 视为关闭。
- `agent.maintainabilityAuditBaseline` 是可选基线，接入时通常写入当前 `HEAD`。
- 如果仓库里已经有 `Maintenance-Audit: true` 标记提交，脚本会优先用它。
- 既没有标记也没有基线的仓库保持安静（避免对从未接入的老仓库立刻报出巨大的未审计计数）。
- 设置环境变量 `AGENT_MAINTAINABILITY_AUDIT_REMINDER=0` 可临时静音。

## 安装方式

### 方式一：机器级（推荐，一次安装全机生效）

把 `.githooks/` 下的脚本复制到 `~/.githooks/` 并保持可执行，然后：

```sh
git config --global core.hooksPath ~/.githooks
git config --global agent.maintainabilityAuditInterval 100
```

之后本机所有仓库的提交都会经过这套 hook；各仓库仍可用本地 `agent.maintainabilityAuditInterval` 覆盖。已存在的无关 hook（如 lefthook、git-lfs 的 shim）不要留在 `~/.githooks/`，否则它们会在每个仓库打印找不到配置的警告。

### 方式二：仓库级（只影响单个仓库）

仓库提交 `.githooks/` 目录，clone 后在仓库根目录执行：

```sh
git config --local core.hooksPath .githooks
```

该命令只设置当前仓库，不修改全局 Git 配置。本仓库（AGENTS）自身采用这种方式。

两种方式的提醒脚本内容相同；机器级安装后更新脚本需要重新复制一次。

## 仓库内的提醒脚本

`.githooks/agent-maintainability-audit-reminder` 已随仓库提供，职责只有三个：

1. 读取当前仓库的本地配置，缺省时回退到全局 `agent.maintainabilityAuditInterval`。
2. 计算距离上次审计还有多少次提交，或者已经超出多少次提交。
3. 打印提醒后退出 0。

已提供以下 Git hook 入口，全部转发到该脚本：

- `post-commit`
- `post-merge`
- `post-rewrite`
- `post-applypatch`
- `post-checkout`

其中 `commit` 是主要场景；其它 hook 用来避免合并、重写历史、切换分支后计数失真。

提示文案统一成两种：

```text
[agent] 建议<N>次后进行项目审计。
[agent] 上次审计是<N>次前，建议尽快安排审计。
```

距上次审计不足 90 次提交时保持安静，避免刚打完审计标记就开始倒数提示；也就是说阈值低于 90 的仓库只会在超期后看到第二种提示。

## 新仓库接入

1. 确认仓库已接入 Git 版本管理。
2. 决定审计间隔是多少次提交（不要按天或按周），写入 `git config --local agent.maintainabilityAuditInterval <N>`；不写则使用全局默认（100）。
3. 如果仓库已经有提交，且没有要求“必须等到显式审计标记后才开始计数”，就把当前 `HEAD` 写成基线：`git config --local agent.maintainabilityAuditBaseline <HEAD_SHA>`。
4. 审计完成时在提交消息里带上 `Maintenance-Audit: true`，作为显式审计标记。

这样接入后，只要用户继续提交，Git 就会在合适的 hook 点提醒是否该审计了。

## 在宿主的 commit instruction 里补一句

如果所用宿主（如 Codex）支持 commit instruction，可以加入这句：

```text
After committing, report audit reminder shown by git hooks.
```

这句的作用是让 agent 在提交完成后把 Git hook 的提醒也带出来，避免用户只看到提交结果却漏掉审计提示。

## 维护约定

- 不要把每个仓库的状态写进 `.githooks/`；状态仍保存在仓库本地 Git 配置和 Git 历史中。
- 不要让提醒阻塞正常提交。
- 不要把“多久提醒一次”做成按天或按周的定时任务，这个问题本质上是 Git 历史长度问题。
- 不要猜测审计点，优先读取显式 `Maintenance-Audit: true` 标记。
- 仓库级安装在新 clone 或新 worktree 里必须各自执行一次 `git config --local core.hooksPath .githooks`，因为 `core.hooksPath` 是本地 Git 配置，不会由 Git 版本控制；机器级安装没有这个问题。

## 最小检查

安装后，至少确认这几件事：

1. `git commit` 后能看到 `[agent]` 提醒（可临时把本地间隔改成 90–100 之间的值并从基线提交 90 次以上来观察）。
2. 审计标记提交后，后续计数会重置。
3. 仓库本地间隔覆盖全局默认；取消本地值后回到全局默认。
