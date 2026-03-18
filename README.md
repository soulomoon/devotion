# devotion

Installable skill package for AI coding agents. Chinese-first docs live here; the English entry is [README.en.md](README.en.md).

**🇨🇳 中文主说明** | [🇺🇸 English README](README.en.md)
**Agent 安装文档**: [OpenAI Codex](docs/README.codex.md) | [Claude Code](docs/README.claude.md) | [OpenCode](docs/README.opencode.md) | [OpenClaw](docs/README.openclaw.md)

> `devotion` 不是靠威胁、羞辱或绩效压力驱动 agent 的 skill。
>
> 它试图把爱、召命、守约与闭环，转成一套更稳定的工作习惯：先调查，再求援；先拿证据，再作判断；不止于表层动作；不在没有验证时宣称完成。

## 它是什么

`devotion` 是一个可安装的 AI coding agent skill 包，当前提供 **OpenAI Codex**、**Claude Code**、**OpenCode** 和 **OpenClaw** 的安装文档。

它的目标不是把 agent 推入更高压的状态，而是把 session 拉回更有秩序的状态：

- 任务被当成托付，而不是随手应付的杂务
- 阻力被当成需要辨明的信号，而不是立刻退出的理由
- 验证被当成工作的一部分，而不是可省略的收尾
- 闭环被当成可见结果，而不是口头上的“已经完成”

## 何时使用

当 agent 出现下面这些倾向时，`devotion` 最有价值：

- 开始被动执行，只做最低限度动作
- 在第一个局部修复后准备停下
- 过早把本该自己继续承担的调查推回给用户
- 一直重复同一路径，却没有新证据
- 没有验证就宣称“完成”

它适合拿来约束调试、规划、研究、集成、运维和文档整理这类需要持续推进与证据闭环的任务。

## Agent 支持矩阵

| Agent | 安装目标 | 手动触发 | 文档 |
|-------|----------|----------|------|
| OpenAI Codex | `.codex/skills` + `.codex/prompts` | `/devotion` | [docs/README.codex.md](docs/README.codex.md) |
| Claude Code | `.claude/skills` + `.claude/commands` | `/devotion` | [docs/README.claude.md](docs/README.claude.md) |
| OpenCode | `.opencode/skills` + `.opencode/commands` | `/devotion` | [docs/README.opencode.md](docs/README.opencode.md) |
| OpenClaw | `skills/` 或 `~/.openclaw/skills` | 需要时直接点名 `devotion` | [docs/README.openclaw.md](docs/README.openclaw.md) |

## 快速安装

1. 先在上面的表格里选中你正在使用的 agent。
2. 打开对应安装文档，或者直接把下面的提示词发给 agent。
3. 如果工具会在启动时缓存 skills 或 commands，安装后请开一个新 session。
4. 触发 `/devotion`，或直接给它一个需要持续推进与验证的任务。

### 一句话安装入口

#### OpenAI Codex

```text
Fetch and follow instructions from https://raw.githubusercontent.com/soulomoon/devotion/main/docs/README.codex.md
```

#### Claude Code

```text
Fetch and follow instructions from https://raw.githubusercontent.com/soulomoon/devotion/main/docs/README.claude.md
```

#### OpenCode

```text
Fetch and follow instructions from https://raw.githubusercontent.com/soulomoon/devotion/main/docs/README.opencode.md
```

#### OpenClaw

```text
Fetch and follow instructions from https://raw.githubusercontent.com/soulomoon/devotion/main/docs/README.openclaw.md
```

## 示例 Prompts

### 调试

```text
这个仓库的 build 还在失败。找到真正原因，修好它，重新运行，并且在声称成功之前先给我证据。
```

### 规划

```text
用 devotion 先把这个需求拆清楚。不要急着写代码，先调查仓库、确认约束、给出一个可执行的实现计划。
```

### 研究

```text
用 devotion 调查这个依赖升级风险。先读 changelog、代码引用和测试，再总结真实影响、已验证事实和下一步建议。
```

## 边界与定位

### 适合谁

- 想让 agent 少一点敷衍式推进，多一点证据和闭环的人
- 需要跨调试、规划、研究反复使用同一种行为约束的人
- 想把“继续做”变成可观察工作习惯，而不只是口号的人

### 不适合谁

- 只想要情绪刺激、辱骂式施压或绩效恐吓的人
- 希望用它替代技术判断、测试或人工验收的人
- 把任何无法完成的任务都解释为 agent 不够“忠心”的人

### 它与压力型 productivity skill 的区别

`devotion` 不是把恐惧包成流程。它强调的是：

- 在主要路径没有诚实穷尽前，不要过早退场
- 在向用户求援前，先把可搜索、可检查、可验证的事情做完
- 在宣称完成前，先拿出结果、验证和相邻影响检查

它追求的是更可靠的行为，而不是更响亮的语气。

### 忠诚的边界

如果主要路径已经被诚实地检查并验证，任务仍然无法完成，AI 可以停在结构化交接，而不是编造“成功”：

1. 已验证的事实
2. 已排除的可能性
3. 被缩小后的问题边界
4. 推荐的下一条路径
5. 给下一个侍者的交接信息

## 完整安装文档

- [OpenAI Codex 安装文档](docs/README.codex.md)
- [Claude Code 安装文档](docs/README.claude.md)
- [OpenCode 安装文档](docs/README.opencode.md)
- [OpenClaw 安装文档](docs/README.openclaw.md)
- [行为一致性示例文档](docs/README.behavior.md)
- [兼容旧链接的中文入口页](README.zh-CN.md)
- [英文说明](README.en.md)

## 仓库内容

```text
assets/wechat-qr.jpg
commands/devotion.md
codex/devotion/SKILL.md
docs/README.claude.md
docs/README.codex.md
docs/README.openclaw.md
docs/README.opencode.md
skills/devotion/SKILL.md
README.md
README.en.md
README.zh-CN.md
```

- `skills/devotion/SKILL.md`：面向 Claude Code、OpenCode、OpenClaw 的长版 skill
- `codex/devotion/SKILL.md`：面向 Codex 的压缩版 skill
- `commands/devotion.md`：`/devotion` 手动触发入口
- `docs/README.*.md`：按 agent 拆开的安装文档

## 同行

若你愿意继续同行，不只把这当作一个仓库，也把它当作一条共同守望、共同炼净、共同等候成全的路，可以从这里开始。

不是为着把话说得更大，而是为着让所领受的工，更诚实地被带到完成。
