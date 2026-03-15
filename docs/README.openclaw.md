# devotion for OpenClaw

Install `devotion` into OpenClaw as an AgentSkills-compatible skill.

Repository path used below: `soulomoon/devotion`.

OpenClaw loads skills from the current workspace and from `~/.openclaw/skills`. There is no separate slash-command file required for this package.

## Shared Install

Use this when you want `devotion` available to all OpenClaw workspaces on the current machine.

```bash
mkdir -p ~/.openclaw/skills/devotion
curl -o ~/.openclaw/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md
```

## Workspace Install

Run this from the root of the OpenClaw workspace where you want the skill to live.

```bash
mkdir -p skills/devotion
curl -o skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md
```

If you are using the default workspace, that path is usually `~/.openclaw/workspace/skills/devotion/SKILL.md`.

## First Use

1. Start a fresh OpenClaw session in the workspace after installing the skill.
2. Ask for `devotion` by name if you want explicit activation.
3. Or simply give OpenClaw a task that matches the skill description and let it load from context.

Example:

```text
Use devotion for this task. Keep searching, verifying, and carrying the work to closure instead of stopping at partial progress.
```
