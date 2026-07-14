---
description: 务实的可维护性优先代码审查
allowed-tools: Bash(git diff --cached:*), Bash(git diff:*), Bash(git status --short:*), Read(*)
---

使用 `pragmatic-review` 核心能力进行审查。

根据用户自然语言解析：
- 范围：默认当前工作区未提交改动；如果用户明确要求暂存区，则只审查暂存区。
- 方向：可选叠加前端、后端、可靠性、架构等审查方向。

输出中文，只报告高信号、可执行、值得修的问题。

工作区状态:
!git status --short

暂存区 diff:
!git diff --cached --unified=0

未暂存 diff:
!git diff --unified=0
