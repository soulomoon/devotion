# Contributing

`devotion` is a small repo, but it has several public entry points that must stay aligned. Treat documentation and install paths as part of the shipped interface.

## Canonical Files

- `skills/devotion/SKILL.md` is the canonical long-form skill text.
- `codex/devotion/SKILL.md` is the compressed Codex variant.
- `commands/devotion.md` is the shared `/devotion` manual trigger entry.
- `docs/README.*.md` are the public install guides.
- `conformance/invariants.json` and `conformance/scenarios/*.json` are the canonical behavioral conformance fixtures.
- `docs/README.behavior.md` is the generated behavior/examples document.
- `README.md`, `README.en.md`, and `README.zh-CN.md` are the public landing pages.

## Maintainer Checklist

Before merging a change, confirm all of the following:

- Trigger conditions still describe the same activation pattern across both skill files.
- The three covenant ideas still match across both skill files, even if the Codex version stays shorter.
- Closure expectations still match across both skill files.
- The conformance invariants still describe the intended behavior claims of the skill package.
- Every scenario still references only defined invariant IDs.
- `docs/README.behavior.md` has been regenerated if any conformance fixture or generator logic changed.
- `commands/devotion.md` still tells the agent to load the installed `devotion` skill and prefer the project-local copy when both local and user-level copies exist.
- Every install guide still points at the correct raw GitHub URLs for the files it installs.
- Every install guide still uses the standard section order:
  - `Install Scope Options`
  - `Commands`
  - `Verify Install`
  - `Update or Reinstall`
  - `Uninstall`
  - `First-Use Example`
  - `Troubleshooting`
- The landing readmes still expose direct links to all four agent guides.
- Public behavior remains the same unless the change explicitly intends to alter it.

## Verification Commands

Run these from the repository root before merging:

```bash
bash tests/check-install-targets.test.sh
./scripts/check-install-targets.sh
bash tests/check-conformance.test.sh
python3 scripts/check-conformance.py
npx --yes markdownlint-cli2 "**/*.md"
```

If you changed install commands, also smoke-test the documented install paths in a disposable directory before merging.

If you changed conformance fixtures or `scripts/check-conformance.py`, regenerate the examples document with:

```bash
python3 scripts/check-conformance.py --write
```
