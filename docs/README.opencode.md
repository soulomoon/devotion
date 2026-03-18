# devotion for OpenCode

Install `devotion` into OpenCode as a skill plus a manual `/devotion` command.

Repository path used below: `soulomoon/devotion`.

OpenCode can also read Claude-compatible and AgentSkills-compatible skill directories, but the native `.opencode` paths are the recommended install target for this package.

## Install Scope Options

| Scope | When to use it | Skill path | Command path |
|-------|----------------|------------|--------------|
| Global | You want `devotion` available across repositories on the current machine | `~/.config/opencode/skills/devotion/SKILL.md` | `~/.config/opencode/commands/devotion.md` |
| Repository-scoped | You want `devotion` pinned to one repository only | `.opencode/skills/devotion/SKILL.md` | `.opencode/commands/devotion.md` |

## Commands

### Global Install

```bash
mkdir -p ~/.config/opencode/skills/devotion
curl -o ~/.config/opencode/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p ~/.config/opencode/commands
curl -o ~/.config/opencode/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

### Repository-Scoped Install

Run this from the repository root where you want the skill to live.

```bash
mkdir -p .opencode/skills/devotion
curl -o .opencode/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p .opencode/commands
curl -o .opencode/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## Verify Install

If you installed globally:

```bash
ls ~/.config/opencode/skills/devotion/SKILL.md ~/.config/opencode/commands/devotion.md
```

If you installed repository-scoped:

```bash
ls .opencode/skills/devotion/SKILL.md .opencode/commands/devotion.md
```

Then start a fresh OpenCode session and run:

```text
/devotion
```

## Update or Reinstall

Re-run the matching install block for the scope you chose. If you are switching scopes, uninstall the old copy first so you know which files OpenCode should load.

## Uninstall

Remove the scope you installed.

Global:

```bash
rm -rf ~/.config/opencode/skills/devotion ~/.config/opencode/commands/devotion.md
```

Repository-scoped:

```bash
rm -rf .opencode/skills/devotion .opencode/commands/devotion.md
```

## First-Use Example

```text
Use devotion. Do not stop at the first shallow fix. Carry this task through verification and closure.
```

## Troubleshooting

- Start a fresh OpenCode session after installing or updating. Some sessions cache skills and commands at startup.
- If `/devotion` does not appear, verify both files exist at the scope you chose.
- If you also keep a Claude-compatible copy around, prefer one clear source of truth for each repository so you know which files OpenCode is actually loading.
