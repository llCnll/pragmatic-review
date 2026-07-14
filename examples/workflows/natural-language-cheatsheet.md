# 自然语言速查表

## 说明

下面这些短句适合团队日常直接复制使用。

原则：
- 已安装 `pragmatic-review` 后，可以直接使用下面短句
- 最稳的句式是：`按<方向>审查<范围>`
- 只写方向，不写范围时，默认会落到“当前未提交改动”

## 高命中短句

### 默认范围

- `审查当前未提交改动`
  作用到：
  - `scope-uncommitted`

- `审查暂存区代码`
  作用到：
  - `scope-staged`

### 前端方向

- `按前端方向审查当前未提交改动`
  作用到：
  - `scope-uncommitted`
  - `lens-frontend`

- `按前端方向审查暂存区代码`
  作用到：
  - `scope-staged`
  - `lens-frontend`

### 后端方向

- `按后端方向审查当前未提交改动`
  作用到：
  - `scope-uncommitted`
  - `lens-backend`

- `按后端方向审查暂存区代码`
  作用到：
  - `scope-staged`
  - `lens-backend`

### 可靠性方向

- `按可靠性方向审查当前未提交改动`
  作用到：
  - `scope-uncommitted`
  - `lens-reliability`

- `按可靠性方向审查暂存区代码`
  作用到：
  - `scope-staged`
  - `lens-reliability`

### 架构方向

- `按架构方向审查当前未提交改动`
  作用到：
  - `scope-uncommitted`
  - `lens-architecture`

- `按架构方向审查暂存区代码`
  作用到：
  - `scope-staged`
  - `lens-architecture`

## 常用组合短句

- `按后端方向和可靠性方向审查当前未提交改动`
  作用到：
  - `scope-uncommitted`
  - `lens-backend`
  - `lens-reliability`

- `按架构方向和后端方向审查当前未提交改动`
  作用到：
  - `scope-uncommitted`
  - `lens-architecture`
  - `lens-backend`

## 输出约束短句

- `只输出最值得修的前 3 条问题`
  作用到：
  - 输出上限约束

- `如果有额外 P0/P1，可以超过 3 条`
  作用到：
  - 高严重级别 override

- `做一次 deep review`
  作用到：
  - 深度模式

## 不够稳定的说法

- `review 一下代码`
  作用到：
  - 默认 `scope-uncommitted`
  - 方向不明确，路由质量较低

- `帮我看看有没有问题`
  作用到：
  - 默认 `scope-uncommitted`
  - 方向不明确，路由质量较低
