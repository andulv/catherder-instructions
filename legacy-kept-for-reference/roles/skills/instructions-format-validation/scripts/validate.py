#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import frontmatter

ALLOWED_TYPES = {"role", "skill", "workflow", "plan", "task", "research", "meta"}
ALLOWED_FRONTMATTER_KEYS = {"type", "description", "alwaysApply"}
ISO_8601_WITH_OFFSET = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$")

REQUIRED_SECTIONS = {
    "plan": ["Goal", "Tasks", "Acceptance Criteria"],
    "task": ["Scope", "Steps", "Verification"],
    "role": ["Summary", "Primary Goals", "Responsibilities"],
    "research": ["Summary", "Findings", "Sources"],
}

SECTION_SYNONYMS = {
    "plan": {
        "Acceptance Criteria": ["Success Criteria"],
        "Tasks": ["Stage 2: Tasks", "Stage 3: Tasks"],
    }
}


def _check(status: str, category: str, check: str, detail: str) -> dict:
    return {"category": category, "check": check, "status": status, "detail": detail}


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def _parse_frontmatter(raw: str) -> tuple[bool, dict, str, str | None]:
    """Returns: has_frontmatter, metadata, body, error"""
    if not raw.startswith("---\n"):
        return False, {}, raw, None

    lines = raw.splitlines(keepends=True)
    closing_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            closing_index = i
            break

    if closing_index is None:
        return True, {}, raw, "Missing closing front-matter delimiter '---'"

    try:
        post = frontmatter.loads(raw)
        body = post.content if isinstance(post.content, str) else ""
        return True, dict(post.metadata), body, None
    except Exception as exc:
        return True, {}, raw, f"Invalid YAML front-matter: {exc}"


def _extract_headings(body: str) -> list[tuple[int, str, int]]:
    headings = []
    for line_no, line in enumerate(body.splitlines(), start=1):
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            headings.append((level, title, line_no))
    return headings


def _check_iso8601(value: str) -> bool:
    if not ISO_8601_WITH_OFFSET.match(value):
        return False
    try:
        dt.datetime.fromisoformat(value)
    except ValueError:
        return False
    return True


def validate_markdown_file(path: Path) -> dict:
    checks: list[dict] = []
    is_reference_doc = "references" in path.parts

    if not path.exists() or not path.is_file():
        return {
            "file": str(path),
            "checks": [
                _check("FAIL", "file", "exists", "Target does not exist or is not a file")
            ],
            "summary": {"pass": 0, "fail": 1, "warn": 0, "uncertain": 0},
        }

    raw = path.read_text(encoding="utf-8")
    basename = path.name
    is_scratchpad = basename == "SCRATCHPAD.md"

    has_frontmatter, metadata, body, fm_error = _parse_frontmatter(raw)

    # Front-matter checks
    if is_scratchpad:
        checks.append(
            _check(
                "PASS",
                "front-matter",
                "scratchpad-exception",
                "SCRATCHPAD.md is exempt from front-matter requirements",
            )
        )
    else:
        if not has_frontmatter:
            checks.append(
                _check("FAIL", "front-matter", "delimiters", "Missing opening front-matter delimiter '---'")
            )
        elif fm_error:
            checks.append(_check("FAIL", "front-matter", "yaml-valid", fm_error))
        else:
            checks.append(_check("PASS", "front-matter", "yaml-valid", "Valid YAML front-matter"))

        if has_frontmatter and not fm_error:
            keys = set(metadata.keys())
            extra_keys = sorted(keys - ALLOWED_FRONTMATTER_KEYS)
            if extra_keys:
                status = "WARN" if is_reference_doc else "FAIL"
                checks.append(
                    _check(
                        status,
                        "front-matter",
                        "unexpected-fields",
                        f"Unexpected front-matter fields: {', '.join(extra_keys)}",
                    )
                )
            else:
                checks.append(_check("PASS", "front-matter", "unexpected-fields", "No unexpected fields"))

            file_type = metadata.get("type")
            if file_type in ALLOWED_TYPES:
                checks.append(_check("PASS", "front-matter", "type", f"type='{file_type}' is allowed"))
            else:
                status = "WARN" if is_reference_doc else "FAIL"
                checks.append(
                    _check(
                        status,
                        "front-matter",
                        "type",
                        f"type must be one of {sorted(ALLOWED_TYPES)}, got: {file_type!r}",
                    )
                )

            description = metadata.get("description")
            if isinstance(description, str) and "\n" not in description and len(description) <= 120:
                checks.append(_check("PASS", "front-matter", "description", "description is one line and <= 120 chars"))
            else:
                checks.append(
                    _check(
                        "FAIL",
                        "front-matter",
                        "description",
                        "description must be a one-line string <= 120 chars",
                    )
                )

            if "alwaysApply" in metadata:
                if isinstance(metadata["alwaysApply"], bool):
                    checks.append(_check("PASS", "front-matter", "alwaysApply-type", "alwaysApply is a boolean"))
                else:
                    checks.append(_check("FAIL", "front-matter", "alwaysApply-type", "alwaysApply must be a boolean"))

    # Heading checks
    headings = _extract_headings(body)
    h1_headings = [title for level, title, _ in headings if level == 1]
    if len(h1_headings) == 1:
        checks.append(_check("PASS", "structure", "one-h1", f"Exactly one H1 heading: '{h1_headings[0]}'"))
    else:
        checks.append(
            _check(
                "FAIL",
                "structure",
                "one-h1",
                f"Expected exactly one H1 heading, found {len(h1_headings)}",
            )
        )

    hierarchy_ok = True
    prev_level = None
    for level, _, _ in headings:
        if prev_level is not None and level > prev_level + 1:
            hierarchy_ok = False
            break
        prev_level = level
    if hierarchy_ok:
        checks.append(_check("PASS", "structure", "heading-hierarchy", "Heading hierarchy is sequential"))
    else:
        checks.append(_check("FAIL", "structure", "heading-hierarchy", "Heading level skip detected"))

    body_lines = body.splitlines()
    bad_blank_lines = 0
    for _, _, line_no in headings:
        idx = line_no - 1
        if idx > 0 and body_lines[idx - 1].strip() != "":
            bad_blank_lines += 1
        if idx < len(body_lines) - 1 and body_lines[idx + 1].strip() != "":
            bad_blank_lines += 1
    if bad_blank_lines == 0:
        checks.append(_check("PASS", "structure", "heading-blank-lines", "Blank lines around headings are valid"))
    else:
        checks.append(
            _check(
                "FAIL",
                "structure",
                "heading-blank-lines",
                f"Found {bad_blank_lines} heading-adjacent missing blank lines",
            )
        )

    normalized_headings = {_normalize(title): title for _, title, _ in headings}

    effective_type = metadata.get("type") if isinstance(metadata, dict) else None
    required = REQUIRED_SECTIONS.get(effective_type, [])
    synonyms = SECTION_SYNONYMS.get(effective_type, {})
    for section in required:
        key = _normalize(section)
        if key in normalized_headings:
            checks.append(_check("PASS", "structure", "required-sections", f"Required section present: '{section}'"))
            continue

        synonym_hits = []
        for syn in synonyms.get(section, []):
            if _normalize(syn) in normalized_headings:
                synonym_hits.append(syn)

        if synonym_hits:
            checks.append(
                _check(
                    "UNCERTAIN",
                    "structure",
                    "required-sections",
                    f"Missing '{section}', found possible synonym(s): {', '.join(synonym_hits)}",
                )
            )
        else:
            checks.append(_check("FAIL", "structure", "required-sections", f"Missing required section: '{section}'"))

    if effective_type in {"skill", "workflow"}:
        h2_or_more = [title for level, title, _ in headings if level >= 2]
        if h2_or_more:
            checks.append(_check("PASS", "structure", "substantive-sections", "At least one substantive section exists"))
        else:
            checks.append(
                _check(
                    "FAIL",
                    "structure",
                    "substantive-sections",
                    "Expected at least one section beyond H1",
                )
            )

    # Naming checks
    if basename == "SCRATCHPAD.md":
        checks.append(_check("PASS", "naming", "scratchpad-name", "SCRATCHPAD.md is a special-case filename"))
    else:
        if re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$", basename):
            checks.append(_check("PASS", "naming", "kebab-case", "Filename is lowercase kebab-case"))
        else:
            checks.append(_check("FAIL", "naming", "kebab-case", "Filename must be lowercase kebab-case"))

    if effective_type == "plan":
        if re.match(r"^\d{3}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$", basename):
            checks.append(_check("PASS", "naming", "plan-pattern", "Plan filename matches NNN-descriptive-name.md"))
        else:
            checks.append(_check("FAIL", "naming", "plan-pattern", "Plan filename must match NNN-descriptive-name.md"))

    if effective_type == "task":
        if re.match(r"^\d{3}[a-z](?:-\d+)?-[a-z0-9]+(?:-[a-z0-9]+)*\.md$", basename):
            checks.append(_check("PASS", "naming", "task-pattern", "Task filename matches expected pattern"))
        else:
            checks.append(_check("FAIL", "naming", "task-pattern", "Task filename must match NNNx-*.md or NNNx-N-*.md"))

    if path.parent.name == path.parent.name.lower():
        checks.append(_check("PASS", "naming", "parent-folder", "Parent folder is lowercase"))
    else:
        checks.append(_check("FAIL", "naming", "parent-folder", "Parent folder name must be lowercase"))

    # Timestamp checks
    timestamp_patterns = [
        (r"^\*\*Created:\*\*\s*(.+)$", "Created"),
        (r"^\*\*Updated:\*\*\s*(.+)$", "Updated"),
        (r"^## Last Updated:\s*(.+)$", "Last Updated"),
    ]

    found_timestamps = []
    for pattern, label in timestamp_patterns:
        for m in re.finditer(pattern, body, flags=re.MULTILINE):
            found_timestamps.append((label, m.group(1).strip()))

    if not found_timestamps:
        checks.append(_check("PASS", "timestamp", "presence", "No timestamp fields found to validate"))
    else:
        for label, value in found_timestamps:
            if _check_iso8601(value):
                checks.append(_check("PASS", "timestamp", "iso8601", f"{label} uses full ISO 8601 with timezone offset"))
            else:
                checks.append(
                    _check(
                        "FAIL",
                        "timestamp",
                        "iso8601",
                        f"{label} must use YYYY-MM-DDTHH:MM:SS+HH:MM, got: {value!r}",
                    )
                )

    summary = {
        "pass": sum(1 for c in checks if c["status"] == "PASS"),
        "fail": sum(1 for c in checks if c["status"] == "FAIL"),
        "warn": sum(1 for c in checks if c["status"] == "WARN"),
        "uncertain": sum(1 for c in checks if c["status"] == "UNCERTAIN"),
    }

    return {"file": str(path), "checks": checks, "summary": summary}


def iter_markdown_files(target: Path) -> list[Path]:
    return sorted(path for path in target.rglob("*.md") if path.is_file())


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic validator for .instructions markdown files")
    parser.add_argument("target", help="Path to a markdown file or directory")
    parser.add_argument("--expected-structures", dest="expected_structures", default=None)
    args = parser.parse_args()

    try:
        target = Path(args.target)

        if not target.exists():
            print(json.dumps({"error": f"Target does not exist: {target}"}, indent=2))
            return 2

        if target.is_dir():
            files = iter_markdown_files(target)
            results = [validate_markdown_file(path) for path in files]
            output = {
                "results": results,
                "summary": {
                    "files_checked": len(results),
                    "pass": sum(item["summary"]["pass"] for item in results),
                    "fail": sum(item["summary"]["fail"] for item in results),
                    "warn": sum(item["summary"]["warn"] for item in results),
                    "uncertain": sum(item["summary"]["uncertain"] for item in results),
                },
            }
            has_failures = any(item["summary"]["fail"] > 0 for item in results)
            print(json.dumps(output, indent=2))
            return 1 if has_failures else 0

        result = validate_markdown_file(target)
        print(json.dumps(result, indent=2))
        return 1 if result["summary"]["fail"] > 0 else 0

    except Exception as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        return 2


if __name__ == "__main__":
    sys.exit(main())
