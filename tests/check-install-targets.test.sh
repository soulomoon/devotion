#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT="$REPO_ROOT/scripts/check-install-targets.sh"

tmp_root="$(mktemp -d)"
trap 'rm -rf "$tmp_root"' EXIT

create_repo() {
  local repo_dir="$1"
  mkdir -p "$repo_dir"
  cd "$repo_dir"
  git init -q
}

expect_success() {
  local repo_dir="$1"
  "$SCRIPT" "$repo_dir"
}

expect_failure() {
  local repo_dir="$1"
  if "$SCRIPT" "$repo_dir"; then
    echo "expected failure for $repo_dir" >&2
    exit 1
  fi
}

valid_repo="$tmp_root/valid"
create_repo "$valid_repo"
mkdir -p "$valid_repo/docs" "$valid_repo/skills/devotion"

cat > "$valid_repo/README.md" <<'EOF'
# Fixture

[Guide](docs/guide.md)
[Skill Raw](https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md)
EOF

cat > "$valid_repo/docs/guide.md" <<'EOF'
# Guide
EOF

cat > "$valid_repo/skills/devotion/SKILL.md" <<'EOF'
# Skill
EOF

git -C "$valid_repo" add README.md docs/guide.md skills/devotion/SKILL.md
expect_success "$valid_repo"

untracked_repo="$tmp_root/untracked"
create_repo "$untracked_repo"
mkdir -p "$untracked_repo/skills/devotion"

cat > "$untracked_repo/README.md" <<'EOF'
# Fixture

[Skill Raw](https://raw.githubusercontent.com/soulomoon/devotion/main/skills/devotion/SKILL.md)
EOF

cat > "$untracked_repo/skills/devotion/SKILL.md" <<'EOF'
# Skill
EOF

git -C "$untracked_repo" add README.md
expect_failure "$untracked_repo"
