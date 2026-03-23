#!/usr/bin/env bash
# SCRIPT_ID:   validate-references.sh
# PURPOSE:     Validate CatHerder reference frontmatter presence for this skill.
# USAGE:       bash scripts/validate-references.sh [skill_path]
# ARGS:        skill_path (optional) - path to skill folder; defaults to parent of scripts/
# OUTPUT:      Human-readable validation results to stdout
# EXIT:        0=all references valid 1=validation issues found 2=usage error
# DEPS:        bash, find, grep, head
set -euo pipefail
skill_path="${1:-$(cd "$(dirname "$0")/.." && pwd)}"
ref_dir="$skill_path/references"
if [[ ! -d "$ref_dir" ]]; then
  echo "references directory not found: $ref_dir"
  exit 1
fi
status=0
while IFS= read -r -d '' f; do
  if ! head -n 5 "$f" | grep -q '^---$'; then
    echo "missing frontmatter: $f"
    status=1
    continue
  fi
  for key in 'type: reference' 'description:' 'snapshot_date:' 'sources:'; do
    if ! grep -q "$key" "$f"; then
      echo "missing $key in $f"
      status=1
    fi
  done
done < <(find "$ref_dir" -maxdepth 1 -type f -name '*.md' -print0)
exit $status
