#!/usr/bin/env bash

set -euo pipefail

repo_root="${1:-$(pwd)}"

python3 - "$repo_root" <<'PY'
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

repo_root = Path(sys.argv[1]).resolve()

raw_url_re = re.compile(
    r"https://raw\.githubusercontent\.com/soulomoon/devotion/main/([A-Za-z0-9._/\-]+)"
)
markdown_link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def git_markdown_files(root: Path) -> list[Path]:
    try:
        output = subprocess.check_output(
            ["git", "-C", str(root), "ls-files", "*.md"], text=True
        )
    except subprocess.CalledProcessError:
        output = ""
    files = [root / line for line in output.splitlines() if line.strip()]
    if files:
        return files
    return sorted(root.rglob("*.md"))


def is_tracked(root: Path, relative_path: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--error-unmatch", str(relative_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def normalize_link_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    if " " in target and not target.startswith(("http://", "https://", "mailto:")):
        target = target.split(" ", 1)[0]
    return target


errors: list[str] = []

for markdown_file in git_markdown_files(repo_root):
    text = markdown_file.read_text(encoding="utf-8")

    for match in raw_url_re.finditer(text):
        raw_path = Path(match.group(1))
        if not (repo_root / raw_path).exists():
            errors.append(
                f"{markdown_file.relative_to(repo_root)}: missing raw install target {raw_path}"
            )
        elif not is_tracked(repo_root, raw_path):
            errors.append(
                f"{markdown_file.relative_to(repo_root)}: raw install target is not tracked {raw_path}"
            )

    for match in markdown_link_re.finditer(text):
        target = normalize_link_target(match.group(1))
        if not target or target.startswith("#"):
            continue
        if target.startswith(("http://", "https://", "mailto:")):
            continue

        parsed = urlparse(target)
        candidate = unquote(parsed.path)
        if not candidate:
            continue

        resolved = (markdown_file.parent / candidate).resolve()
        if not resolved.exists():
            errors.append(
                f"{markdown_file.relative_to(repo_root)}: broken local link {candidate}"
            )

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(git_markdown_files(repo_root))} Markdown files in {repo_root}")
PY
