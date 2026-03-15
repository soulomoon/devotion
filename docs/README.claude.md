# devotion for Claude Code

Install `devotion` into Claude Code as a skill plus a manual `/devotion` slash command.

Repository path used below: `soulomoon/devotion`.

## Global Install

Use this when you want `devotion` available across repositories on the current machine.

```bash
mkdir -p ~/.claude/skills/devotion
curl -o ~/.claude/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## Project Install

Use this when you want `devotion` checked into the current repository for the team.

```bash
mkdir -p .claude/skills/devotion
curl -o .claude/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p .claude/commands
curl -o .claude/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## First Use

1. Start a fresh Claude Code session if Claude was already open.
2. Type `/devotion` for explicit activation.
3. Or simply give Claude a task that matches the `devotion` description and let the skill auto-load.

Example:

```text
The agent is stopping too early in this repo. Use devotion, keep going until the main paths are exhausted, and show evidence before you say you are done.
```
