# devotion for OpenCode

Install `devotion` into OpenCode as a skill plus a manual `/devotion` command.

Repository path used below: `soulomoon/devotion`.

OpenCode can also read Claude and AgentSkills-compatible skill directories, but the native `.opencode` paths are the recommended install target.

## Global Install

Use this when you want `devotion` available across repositories on the current machine.

```bash
mkdir -p ~/.config/opencode/skills/devotion
curl -o ~/.config/opencode/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p ~/.config/opencode/commands
curl -o ~/.config/opencode/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## Project Install

Use this when you want `devotion` pinned to the current repository only.

```bash
mkdir -p .opencode/skills/devotion
curl -o .opencode/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md

mkdir -p .opencode/commands
curl -o .opencode/commands/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## First Use

1. Start a fresh OpenCode session if OpenCode was already open.
2. Type `/devotion` for explicit activation.
3. Or ask OpenCode to use the `devotion` skill if you want to trigger it by name.

Example:

```text
Use devotion. Do not stop at the first shallow fix. Carry this task through verification and closure.
```
