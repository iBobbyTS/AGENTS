# PLAN-FULL — 示例业务功能

- Feature: example-feature
- Status: PLANNED
- Repository / feature base / target / current branch: 由实际 Git 填写
- Execution mode: EXECUTE_WITH_COMMIT
- Mode rule: 只要使用 SFD，执行始终采用 EXECUTE_WITH_COMMIT；即使单节也在独立非 main feature branch 上提交。PLAN_HANDOFF 仅交付计划，不自行写产品代码。
- Branch authority: 用户批准的独立 feature branch
- Task intent: IMPLEMENT / PLAN_HANDOFF / REVIEW_ONLY（按真实请求选择，不是执行模式）
- Installation target / home: 从已安装 installation.json 读取
- Dispatch profile: 本安装的唯一 profile（installation.json）
- Reviewer routes (A/B, actual native/external transport): 从内嵌 profile 复制；PLAN 和 code 分别配置
- Main identity / observed model: 真实证据；缺失为 UNKNOWN
- Invocation: USER_EXPLICIT
- Requirements: .agent-work/REQUIREMENTS.md

## 目标、权威与排除项

写原始业务结果、已确认修正、真实输入/反例、现有生产合同与最小充分实现。 不由 PLAN 自创需求，不为审核回执添加产品机制。

## 规划知识路由与边界样例

- 规划路由：列实际命中的 Domain / Language / Adapter / Concern 与必要指南；明确已有知识或缺口。只在路由不明时查规划索引（references/planning/index.md），不逐轮重读。
- Domain / Language / Adapter / Concern：各写实际读取的命中文件与源码理由；未适用写 NOT_APPLICABLE，已有指南覆盖相同问题可写 COVERED_BY。
- Universal fallback：not needed，或明确尚未覆盖的技术/边界及理由；先保留并读取所有独立命中项，不能因一个未知后端就整项只用 universal。
- 多个模块合并到同一计划；选中资料不是新需求，不为每个模块新建 section、测试或 review。
- 真实边界（如无则省略）：权威 → producer/serializer → 输入样例 → 状态/响应 → 实际 consumer → 可判错检查。
- 样例来源：SOURCE_INSPECTED / OBSERVED / PLANNED / UNKNOWN；未实施接口不能伪装已运行。
- 明确需求点名的读者：EDIT / VERIFY_UNCHANGED / OUT_OF_SCOPE 及必要理由；生产者 HANDOFF 和消费者 TASK 复用同一份样例。

本段是人可读内容，没有新 JSON、路由校验器或审批门禁。一个局部改动不需要填满所有技术清单。

<!-- 仅命中 long-horizon.md 时：在本文件加入完整剩余结果→section 映射、少量真实组合里程碑、已接受/partial 基线与当前工作窗口。所有单元仍写具体 impl/dependency；普通功能删除本注释即可，不必新增章节。 -->

## 调度与最终验证

- 顺序：S01，然后 S02。
- 并行：本例串行；允许并行时明确路径、契约和测试资源无冲突。
- 最终测试/发布环境/尚未证明的组合路径：填具体行为，不建“收尾一切”的证据专用节。

## S01 — 第一项业务结果
- Implementer: impl_std
- Depends on: none
- Feature slug（仅当仓内产物命名需要区分时填写）：

### 业务合同

- 权威、产出及实际 consumer：
- 修改 owner / inspect-only / exclusions：
- 不变量与安全中间态：
- 任务模型依据：范例、歧义、状态耦合、新推理、可判错测试。
- AC、targeted/section 检查：
- Review：BOUNDED；固定两份独立 clean 覆盖，槽位规则（含沉默槽退役）见 reviewer-orchestration.md。

## S02 — 第二项业务结果
- Implementer: impl_large
- Depends on: S01

### 父级合同

- 完整业务结果、跨子项不变量、joint oracle：
- 拆分依据：真实内部模块或模型能力，不拆散同一验收合同。
- 父级 review/repair budget：共享原 lineage，不给子项新配额。
- Review：固定两轮 clean，子项证据在父级累计。

### S02.A — 内部基础模块
- Implementer: impl_large
- Depends on: none

- 模型理由、改动边界、产出/consumer、安全中间态、具体检查：

### S02.B — 内部消费者
- Implementer: impl_std
- Depends on: S02.A

- 模型理由、改动边界、产出/consumer、安全中间态、具体检查：

## 集成与完成

父级 reconciliation 与独立 coverage pair（Clean A + Clean B）通过才接受 S02。验证组装后的 product/test head，记录实际结果和缺口，然后关闭并归档到 .agent-work/archive/{YYYYMMDD-HHMM_feature-id}/：PLAN-FULL 连同需保留的真实证据（原始需求、终态 FEATURE-STATE（含 efficiency log）、评审报告、HANDOFF），删除可从 PLAN-FULL 重建的派发视图（PLAN 摘录、section/task 拆分件）。后续用户请求默认重新评估。
