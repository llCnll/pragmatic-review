# 工程模式索引

本目录维护通用工程决策的适用场景、选项、限制、来源与最小验证。项目规则和已确认契约优先，模式按当前问题选择；实施指导可单独读取，评审按观察到的变化点加载。

[质量基线](../engineering-guidelines.md)维护通用判断，[检查模块](../../prompts/routing/review-router.md)选择评审方法。

## 按问题选择

| 问题 | 模式 |
| --- | --- |
| 分层与模块边界 | [分层](layering-patterns.md)，多供应商边界为试用中 |
| 装配与能力登记 | [组合根](composition-root-patterns.md)，试用中 |
| 复杂业务分支 | [语义拆分](branch-complexity-patterns.md)，试用中 |
| 多状态与副作用重构 | [受控重构](refactoring-patterns.md)，试用中 |
| 查询与数据访问 | [查询](query-patterns.md) |
| 手写 SQL 和动态标识 | [SQL 安全](sql-safety-patterns.md) |
| 迁移与数据修复 | [数据库变更](database-change-patterns.md)，批量修复为试用中 |
| 历史响应与新约束 | [响应兼容](response-compatibility-patterns.md)，试用中 |
| 接口业务语义与字段投影 | [接口设计](api-patterns.md)，页面字段投影为试用中 |
| 失败与重试边界 | [错误处理](error-handling-patterns.md)，异步恢复为试用中 |
| 根因、关联与脱敏 | [日志](logging-patterns.md)，试用中 |
| 跨框架界面与状态 | [UI 借鉴](cross-platform-ui-patterns.md)，试用中 |

只读取匹配模式，核对适用前提与限制；实际验证和未覆盖事项留在项目记录。模式升级记录可重复证据、适用范围、限制与实际验证状态，保持本目录为工程模式的唯一维护源。
