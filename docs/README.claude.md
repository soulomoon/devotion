# devotion for Claude Code

Install `devotion` into Claude Code as a skill plus a manual `/devotion` slash command.

Repository path used below: `soulomoon/devotion`.

## Install Scope Options

| Scope | When to use it | Skill path | Command path |
|-------|----------------|------------|--------------|
| Global | You want `devotion` available across repositories on the current machine | `~/.claude/skills/devotion/SKILL.md` | `~/.claude/commands/devotion.md` |
| Repository-scoped | You want `devotion` checked into one repository for the team | `.claude/skills/devotion/SKILL.md` | `.claude/commands/devotion.md` |

## Commands

### Global Install

```bash
mkdir -p ~/.claude/skills/devotion
curl -o ~/.claude/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p ~/.claude/commands
curl -o ~/.claude/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

### Repository-Scoped Install

Run this from the repository root where you want the skill to live.

```bash
mkdir -p .claude/skills/devotion
curl -o .claude/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p .claude/commands
curl -o .claude/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## Verify Install

If you installed globally:

```bash
ls ~/.claude/skills/devotion/SKILL.md ~/.claude/commands/devotion.md
```

If you installed repository-scoped:

```bash
ls .claude/skills/devotion/SKILL.md .claude/commands/devotion.md
```

Then start a fresh Claude Code session and run:

```text
/devotion
```

## Update or Reinstall

Re-run the matching install block for the scope you chose. If you are switching scopes, uninstall the old copy first so you know which files Claude Code should load.

## Uninstall

Remove the scope you installed.

Global:

```bash
rm -rf ~/.claude/skills/devotion ~/.claude/commands/devotion.md
```

Repository-scoped:

```bash
rm -rf .claude/skills/devotion .claude/commands/devotion.md
```

## First-Use Example

```text
The agent is stopping too early in this repo. Use devotion, keep going until the main paths are honestly exhausted, and show evidence before you say you are done.
```

## Troubleshooting

- Start a fresh Claude Code session after installing or updating. Some sessions cache skills and commands at startup.
- If `/devotion` does not appear, verify both files exist at the scope you chose.
- If both a repository-local copy and a user-level copy exist, keep the repository-local one aligned with the repo so there is no ambiguity about which version should win.
