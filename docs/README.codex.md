# devotion for Codex

Install `devotion` into OpenAI Codex as a skill plus a manual `/devotion` prompt.

Repository path used below: `soulomoon/devotion`.

## Global Install

Use this when you want `devotion` available across repositories on the current machine.

```bash
mkdir -p ~/.codex/skills/devotion
curl -o ~/.codex/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/codex/devotion/SKILL.md

mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## Repository-Scoped Install

Use this when you want `devotion` pinned to the current repository only.

```bash
mkdir -p .codex/skills/devotion
curl -o .codex/skills/devotion/SKILL.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/codex/devotion/SKILL.md

mkdir -p .codex/prompts
curl -o .codex/prompts/devotion.md \
  https://raw.githubusercontent.com/soulomoon/devotion/main/commands/devotion.md
```

## First Use

1. Start a fresh Codex session if Codex was already open.
2. Type `/devotion`.
3. Give it a task that requires persistence and verification.

Example:

```text
There is a failing build in this repo. Find the real cause, fix it, rerun it, and show evidence before you claim success.
```
