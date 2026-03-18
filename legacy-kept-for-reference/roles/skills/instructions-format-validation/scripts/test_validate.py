import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from validate import validate_markdown_file


SCRIPT_PATH = Path(__file__).resolve().parent / "validate.py"


class ValidateScriptTests(unittest.TestCase):
    def _write(self, directory: Path, name: str, content: str) -> Path:
        path = directory / name
        path.write_text(content, encoding="utf-8")
        return path

    def _statuses(self, result):
        return [item["status"] for item in result["checks"]]

    def _find_check(self, result, category, check):
        for item in result["checks"]:
            if item["category"] == category and item["check"] == check:
                return item
        return None

    def test_valid_plan_file(self):
        content = """---
type: plan
description: \"Valid plan\"
---
# Plan 001: Sample

**Status:** in-progress

**Branch:** feature/001-sample

**Created:** 2026-03-04T10:00:00+00:00

**Updated:** 2026-03-04T10:30:00+00:00

## Goal

Do thing.

## Tasks

- [ ] Item

## Acceptance Criteria

- Works
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "001-sample-plan.md", content)
            result = validate_markdown_file(path)
            self.assertGreater(result["summary"]["pass"], 0)
            self.assertEqual(result["summary"]["fail"], 0)

    def test_missing_frontmatter_fails(self):
        content = """# Task 008f: Example

## Scope

x

## Steps

x

## Verification

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-example.md", content)
            result = validate_markdown_file(path)
            front = self._find_check(result, "front-matter", "delimiters")
            self.assertIsNotNone(front)
            self.assertEqual(front["status"], "FAIL")

    def test_invalid_yaml_fails(self):
        content = """---
type: task
description: \"ok\n---
# Task 008f: Example

## Scope

x

## Steps

x

## Verification

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-example.md", content)
            result = validate_markdown_file(path)
            yaml_check = self._find_check(result, "front-matter", "yaml-valid")
            self.assertIsNotNone(yaml_check)
            self.assertEqual(yaml_check["status"], "FAIL")

    def test_wrong_type_fails(self):
        content = """---
type: knowledge
description: \"desc\"
---
# Task 008f: Example

## Scope

x

## Steps

x

## Verification

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-example.md", content)
            result = validate_markdown_file(path)
            type_check = self._find_check(result, "front-matter", "type")
            self.assertEqual(type_check["status"], "FAIL")

    def test_description_over_120_fails(self):
        long_desc = "a" * 121
        content = f"""---
type: task
description: \"{long_desc}\"
---
# Task 008f: Example

## Scope

x

## Steps

x

## Verification

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-example.md", content)
            result = validate_markdown_file(path)
            desc_check = self._find_check(result, "front-matter", "description")
            self.assertEqual(desc_check["status"], "FAIL")

    def test_uppercase_filename_fails_naming(self):
        content = """---
type: task
description: \"desc\"
---
# Task 008f: Example

## Scope

x

## Steps

x

## Verification

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-Example.md", content)
            result = validate_markdown_file(path)
            naming = self._find_check(result, "naming", "kebab-case")
            self.assertEqual(naming["status"], "FAIL")

    def test_skipped_heading_level_fails(self):
        content = """---
type: task
description: \"desc\"
---
# Task 008f: Example

### Scope

x

## Steps

x

## Verification

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-example.md", content)
            result = validate_markdown_file(path)
            heading = self._find_check(result, "structure", "heading-hierarchy")
            self.assertEqual(heading["status"], "FAIL")

    def test_missing_required_section_fails(self):
        content = """---
type: task
description: \"desc\"
---
# Task 008f: Example

## Scope

x

## Steps

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008f-example.md", content)
            result = validate_markdown_file(path)
            required = [
                item
                for item in result["checks"]
                if item["category"] == "structure"
                and item["check"] == "required-sections"
                and "Verification" in item["detail"]
            ]
            self.assertTrue(required)
            self.assertEqual(required[0]["status"], "FAIL")

    def test_synonym_section_name_uncertain(self):
        content = """---
type: plan
description: \"desc\"
---
# Plan 008: Example

**Created:** 2026-03-04T10:00:00+00:00

**Updated:** 2026-03-04T10:30:00+00:00

## Goal

x

## Stage 2: Tasks

x

## Success Criteria

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008-example.md", content)
            result = validate_markdown_file(path)
            uncertain = [item for item in result["checks"] if item["status"] == "UNCERTAIN"]
            self.assertTrue(uncertain)

    def test_bare_date_timestamp_fails(self):
        content = """---
type: plan
description: \"desc\"
---
# Plan 008: Example

**Created:** 2026-03-04

**Updated:** 2026-03-04T10:30:00+00:00

## Goal

x

## Tasks

x

## Acceptance Criteria

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008-example.md", content)
            result = validate_markdown_file(path)
            fails = [item for item in result["checks"] if item["category"] == "timestamp" and item["status"] == "FAIL"]
            self.assertTrue(fails)

    def test_valid_iso_timestamp_passes(self):
        content = """---
type: plan
description: \"desc\"
---
# Plan 008: Example

**Created:** 2026-03-04T10:00:00+00:00

**Updated:** 2026-03-04T10:30:00+00:00

## Goal

x

## Tasks

x

## Acceptance Criteria

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "008-example.md", content)
            result = validate_markdown_file(path)
            fails = [item for item in result["checks"] if item["category"] == "timestamp" and item["status"] == "FAIL"]
            self.assertFalse(fails)

    def test_scratchpad_frontmatter_skipped(self):
        content = """# Scratchpad

## Last Updated: 2026-03-04T10:30:00+00:00

## Current Context

x
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "SCRATCHPAD.md", content)
            result = validate_markdown_file(path)
            check = self._find_check(result, "front-matter", "scratchpad-exception")
            self.assertIsNotNone(check)
            self.assertEqual(check["status"], "PASS")

    def test_cli_exit_code_one_on_fail(self):
        content = """# broken
"""
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self._write(Path(temp_dir), "bad.md", content)
            proc = subprocess.run(
                [str(Path(__file__).resolve().parent.parent.parent.parent.parent / ".venv/bin/python"), str(SCRIPT_PATH), str(path)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 1)
            parsed = json.loads(proc.stdout)
            self.assertIn("summary", parsed)


if __name__ == "__main__":
    unittest.main()
