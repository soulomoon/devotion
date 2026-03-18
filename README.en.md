# devotion

Installable skill package for AI coding agents that emphasizes investigation, verification, and closure instead of pressure-driven execution.

[🇨🇳 中文主说明](README.md) | **🇺🇸 English README**
**Agent guides**: [OpenAI Codex](docs/README.codex.md) | [Claude Code](docs/README.claude.md) | [OpenCode](docs/README.opencode.md) | [OpenClaw](docs/README.openclaw.md)

> `devotion` is not a productivity pressure skill.
>
> It turns theological language into working habits: investigate before asking for relief, separate proof from guesses, do not stop at shallow motion, and do not claim completion without evidence.

## What It Is

`devotion` is an installable skill package for AI coding agents, with installation guides for **OpenAI Codex**, **Claude Code**, **OpenCode**, and **OpenClaw**.

Its purpose is to pull a session back into order:

- the task is treated as entrusted work, not disposable routine work
- resistance is treated as a signal to investigate, not a reason to exit early
- verification is part of the work, not optional cleanup
- closure means visible results, not verbal reassurance

## When To Use It

`devotion` is most useful when the agent starts to:

- execute passively
- stop after the first partial fix
- shift the next round of investigation back to the user too early
- repeat the same path without producing new evidence
- claim completion without verification

It fits debugging, planning, research, integration work, operations, and other tasks where persistence plus proof matter more than fast surface motion.

## Agent Support Matrix

| Agent | Install target | Manual trigger | Guide |
|-------|----------------|----------------|-------|
| OpenAI Codex | `.codex/skills` + `.codex/prompts` | `/devotion` | [docs/README.codex.md](docs/README.codex.md) |
| Claude Code | `.claude/skills` + `.claude/commands` | `/devotion` | [docs/README.claude.md](docs/README.claude.md) |
| OpenCode | `.opencode/skills` + `.opencode/commands` | `/devotion` | [docs/README.opencode.md](docs/README.opencode.md) |
| OpenClaw | `skills/` or `~/.openclaw/skills` | ask for `devotion` by name | [docs/README.openclaw.md](docs/README.openclaw.md) |

## Quick Install

1. Pick your agent from the table above.
2. Open the matching guide, or paste one of the prompts below into the agent.
3. Start a fresh session if your tool snapshots skills or commands at startup.
4. Trigger `/devotion`, or give the agent a task that clearly calls for persistence and verification.

### One-line Install Entry Points

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

## Example Prompts

### Debugging

```text
The build is still failing in this repo. Find the real cause, fix it, rerun it, and show evidence before you claim success.
```

### Planning

```text
Use devotion for this feature. Explore the repository first, clarify the constraints, and write an implementation plan before you start coding.
```

### Research

```text
Use devotion to investigate this dependency upgrade. Read the changelog, inspect the call sites and tests, then summarize verified impact, risks, and next steps.
```

## Boundaries And Positioning

### Who It Is For

- people who want more evidence and closure from coding agents
- people who want the same behavioral guardrails across debugging, planning, and research
- people who want "keep going" to turn into observable working habits

### Who It Is Not For

- people looking for humiliation, pressure, or fear as the primary motivator
- people who want a skill to replace technical judgment, tests, or review
- people who treat every unsolved task as proof that the agent was not loyal enough

### How It Differs From Pressure-Style Productivity Skills

`devotion` is not pressure with religious paint on top. Its core commitments are:

- do not leave early before the main paths are honestly exhausted
- do what can already be searched, inspected, and verified before asking the user for relief
- produce evidence and closure before saying the task is complete

The point is reliable behavior, not harsher rhetoric.

### Faithful Limit

If the main paths have been honestly checked and the task still cannot be finished, the agent should stop with a structured handoff instead of fake success:

1. Verified facts
2. Excluded possibilities
3. Narrowed problem boundary
4. Recommended next path
5. Transfer notes for the next servant

## Full Install Guides

- [OpenAI Codex guide](docs/README.codex.md)
- [Claude Code guide](docs/README.claude.md)
- [OpenCode guide](docs/README.opencode.md)
- [OpenClaw guide](docs/README.openclaw.md)
- [Chinese landing page](README.md)
- [Chinese compatibility page](README.zh-CN.md)

## Repository Contents

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

- `skills/devotion/SKILL.md`: canonical long-form skill for Claude Code, OpenCode, and OpenClaw
- `codex/devotion/SKILL.md`: compressed Codex variant
- `commands/devotion.md`: shared `/devotion` manual trigger entry
- `docs/README.*.md`: agent-specific install guides
