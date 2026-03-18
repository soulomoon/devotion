# devotion for OpenAI Codex

Install `devotion` into OpenAI Codex as a skill plus a manual `/devotion` prompt.

Repository path used below: `soulomoon/devotion`.

## Install Scope Options

| Scope | When to use it | Skill path | Prompt path |
|-------|----------------|------------|-------------|
| Global | You want `devotion` available across repositories on the current machine | `~/.codex/skills/devotion/SKILL.md` | `~/.codex/prompts/devotion.md` |
| Repository-scoped | You want `devotion` pinned to one repository only | `.codex/skills/devotion/SKILL.md` | `.codex/prompts/devotion.md` |

## Commands

### Global Install

```bash
mkdir -p ~/.codex/skills/devotion
curl -o ~/.codex/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/codex/devotion/SKILL.md

mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

### Repository-Scoped Install

Run this from the repository root where you want the skill to live.

```bash
mkdir -p .codex/skills/devotion
curl -o .codex/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/codex/devotion/SKILL.md

mkdir -p .codex/prompts
curl -o .codex/prompts/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## Verify Install

If you installed globally:

```bash
ls ~/.codex/skills/devotion/SKILL.md ~/.codex/prompts/devotion.md
```

If you installed repository-scoped:

```bash
ls .codex/skills/devotion/SKILL.md .codex/prompts/devotion.md
```

Then start a fresh Codex session and run:

```text
/devotion
```

## Update or Reinstall

Re-run the matching install block for the scope you chose. If you are switching from one scope to the other, uninstall the old copy first so you know which files Codex is loading.

## Uninstall

Remove the scope you installed.

Global:

```bash
rm -rf ~/.codex/skills/devotion ~/.codex/prompts/devotion.md
```

Repository-scoped:

```bash
rm -rf .codex/skills/devotion .codex/prompts/devotion.md
```

## First-Use Example

```text
There is a failing build in this repo. Find the real cause, fix it, rerun it, and show evidence before you claim success.
```

## Troubleshooting

- Start a fresh Codex session after installing or updating. Some sessions cache skills and prompts at startup.
- If `/devotion` does not appear, verify both files exist at the scope you chose.
- If both a repository-local copy and a user-level copy exist, the repository-local one should be the clearer source of truth for that repo.
