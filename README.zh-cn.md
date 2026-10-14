# AGENTS.md

[英文版](README.md)

个人使用的Coding Agent约束，作为备份和分享。<br>
本README纯手打，无AI，仓库内其余文件基本 100%AI。英文版为GPT 6.1 Sol翻译。

## 目录

- [AGENTS.md](#agentsmd文件)
- [Git Hook](#git-hook)
- [Skills](#skills)
    ### Sectioned Feature Development
    - [grill-me](#grill-me): 先挖掘需求，不问产品架构。
    - [sectioned-feature-development](#sectioned-feature-development): 分块开发大功能，含planning知识库。
    - [code-review](#code-review): 一次功能修改后的代码审核。
    ### Quality Control
    - [quality-steward](#quality-steward): 是否对目标项目启动审计的检测，建议自动化定期运行。
    - [general-audit](#general-audit): 定期项目审计，含审计知识库。
    - [deployment-preflight](#deployment-preflight): 部署前检查。
    ### Debug
    - [adaptive-debugging](#adaptive-debugging): 第一次修复失败后走这个流程，包含debug知识库。
    - [debug-notes-to-engineering-notes](#debug-notes-to-engineering-notes): 仅在官方文档不全/有误时才使用，结合[adaptive-debugging](#adaptive-debugging)，燃烧自己的token，为后人照亮debug之路。
    ### 其它工具
    - [feishu-message-sender](#feishu-message-sender): 飞书自定义机器人在长任务里定时汇报


## AGENTS.md文件
[AGENTS.md](AGENTS.md) 是 Codex, Zcode 等 agent 默认读取的约束名，总共有2层 `AGENTS.md`，一个在 `~/.codex/AGENTS.md`，另一个在项目的根目录里。


主要职责：

【待填写】

## Git Hook

Hook 脚本已随仓库提供；clone 后在仓库根目录执行 `./scripts/install-git-hooks.sh` 即可为当前仓库启用。[git-hook.md](docs/git-hook.md) 说明配置与验证方式。
- 每次审计完成时提交消息带上 `Maintenance-Audit: true`。
- 提醒脚本位于 `.githooks/`，不依赖用户目录中的绝对路径。
- 每次提交时Git会提醒下次审计什么时候或已经超过了设定间隔。

## Skills

### Sectioned Feature Development

#### [grill-me](skills/grill-me)
用户需要可以描述清楚自己的需求，Agent用这个skill只问用户没描述清的部分，不问架构/代码层面的问题。
> This skill is an independently rewritten, requirements-focused adaptation inspired by Matt Pocock's `grill-me` / `grilling` skills from https://github.com/mattpocock/skills. The upstream project is licensed under the MIT License. Upstream copyright: Copyright (c) 2026 Matt Pocock
#### [sectioned-feature-development](skills/sectioned-feature-development/)

对于大功能，必须先制定完整计划，再分section实现，大致流程如下：

```c
skill sectioned_feature_development() {
    主 Agent 创建完整计划，拆分section/subsection，决定对应的模型;
    GPT 6 Astra (Xhigh) 执行 Plan Review;
    for section in sections {
        拆分section到单独的文件;
        switch (section定义) {
            case impl_std:
                DeepSeek V4.1 Flash (high) 实现;
            case impl_large:
                GPT 6.1 Sol (high) 实现;
        }
        while (true) {  // Code review循环
            调用 GLM 5.3 使用 $code-review 进行审查;
            没问题后用 GPT 6.1 Sol 再审查;
            if 循环次数 > 5 {
                打包advisor_pack给GPT 6 Astra Pro裁决;
                break;
            }
        }
    }
}
```

#### [code-review](skills/code-review/)

GPT 5.6 Sol Pro 自己写的，我没有看过具体内容，实战下来挺好用的。

### Quality Control

#### [quality-steward](skills/quality-steward)
适合自动化运行，配置好需要审查的仓库，每次agent启动时自动在这些仓库看提交需不需要审计。建议给Flash级别模型去做，不需要太强推理能力。

#### [general-audit](skills/general-audit/)

`GPT 6 Astra Pro` 上网调研并制定的审计方式。包含大部分审计面。

#### [deployment-preflight](skills/deployment-preflight)

检查部署安全，数据库会不会丢数据等。

### Debug

#### [adaptive-debugging](skills/adaptive-debugging/)
包含Debug知识库。
先做“证据盘点”，包括上一轮改了什么、为什么没解决、现在的失败现象是什么、有没有可运行复现。然后再进原 
新增流程：把试错过程记录在`.agent-work/debug`下，避免疑难杂症经历过多次上下文压缩后忘记之前试过的错误路径。

#### [debug-notes-to-engineering-notes](skills/debug-notes-to-engineering-notes)

使用[adaptive-debugging](#adaptive-debugging)修完问题后把 `.agent-work/debug` 里的记录沉淀到 `docs/engineering-notes`，方便后续开发和其他人阅读。会记录正确做法、错误尝试记录、和官方文档不符的部分、版本记录。不包含项目/实现约定。

### 其它工具

#### [feishu-message-sender](skills/feishu-message-sender)

建议长任务时使用，不要让agent在前台轮询。使用这个skill它会复制一份模板脚本，然后编辑脚本并后台启动，用你的飞书机器人发送一条任务开始通知、每小时的进度汇报、任务结束总结。<br>
机器人配置放在 `~/.config/feishu-message-sender/secret.json`，格式为`{"webhook":"https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxxxxxx","secret":"签名秘钥","name":"本电脑的名字"}`。<br>
飞书官方：[自定义机器人使用指南](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot?lang=zh-CN)（给agent看的话用[md版本](https://open.feishu.cn/document/client-docs/bot-v3/add-custom-bot.md)）
