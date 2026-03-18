# devotion for OpenClaw

Install `devotion` into OpenClaw as an AgentSkills-compatible skill.

Repository path used below: `soulomoon/devotion`.

OpenClaw loads skills from the current workspace and from `~/.openclaw/skills`. This package does not require a separate slash-command file.

## Install Scope Options

| Scope | When to use it | Skill path | Manual trigger |
|-------|----------------|------------|----------------|
| Shared | You want `devotion` available to all OpenClaw workspaces on the current machine | `~/.openclaw/skills/devotion/SKILL.md` | Ask for `devotion` by name |
| Workspace-scoped | You want `devotion` pinned to one OpenClaw workspace only | `skills/devotion/SKILL.md` | Ask for `devotion` by name |

## Commands

### Shared Install

```bash
mkdir -p ~/.openclaw/skills/devotion
curl -o ~/.openclaw/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md
```

### Workspace-Scoped Install

Run this from the root of the OpenClaw workspace where you want the skill to live.

```bash
mkdir -p skills/devotion
curl -o skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md
```

If you are using the default workspace, that path is usually `~/.openclaw/workspace/skills/devotion/SKILL.md`.

## Verify Install

If you installed the shared copy:

```bash
ls ~/.openclaw/skills/devotion/SKILL.md
```

If you installed the workspace copy:

```bash
ls skills/devotion/SKILL.md
```

Then start a fresh OpenClaw session in the workspace and ask for:

```text
Use devotion for this task.
```

## Update or Reinstall

Re-run the matching install block for the scope you chose. If you move from a shared copy to a workspace copy, remove the old one first so you know which version OpenClaw is reading.

## Uninstall

Remove the scope you installed.

Shared:

```bash
rm -rf ~/.openclaw/skills/devotion
```

Workspace-scoped:

```bash
rm -rf skills/devotion
```

## First-Use Example

```text
Use devotion for this task. Keep searching, verifying, and carrying the work to closure instead of stopping at partial progress.
```

## Troubleshooting

- Start a fresh OpenClaw session in the target workspace after installing or updating.
- If the skill does not load, verify the `SKILL.md` file exists in the shared or workspace path you intended to use.
- If both shared and workspace copies exist, keep the workspace copy aligned with the repo when you want one workspace to override the global default.
