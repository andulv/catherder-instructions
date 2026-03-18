import tempfile
import unittest
from pathlib import Path

from validate_references import validate_references


class ValidateReferencesTests(unittest.TestCase):
    def _write(self, root: Path, rel: str, content: str):
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_detects_missing_markdown_link_target(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            file_path = self._write(
                root,
                ".instructions/a.md",
                "# A\n\nSee [missing](missing.md).\n",
            )
            result = validate_references(file_path, workspace_root=root)
            self.assertEqual(result["summary"]["broken"], 1)
            self.assertEqual(result["findings"][0]["code"], "FILE_NOT_FOUND")

    def test_detects_missing_anchor(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            file_path = self._write(
                root,
                ".instructions/a.md",
                "# A\n\nGo [there](b.md#nope).\n",
            )
            self._write(root, ".instructions/b.md", "# B\n\n## Exists\n")
            result = validate_references(file_path, workspace_root=root)
            self.assertEqual(result["summary"]["broken"], 1)
            self.assertEqual(result["findings"][0]["code"], "ANCHOR_NOT_FOUND")

    def test_passes_for_valid_local_links(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            file_path = self._write(
                root,
                ".instructions/a.md",
                "# A\n\nGo [there](b.md#exists).\n",
            )
            self._write(root, ".instructions/b.md", "# B\n\n## Exists\n")
            result = validate_references(file_path, workspace_root=root)
            self.assertEqual(result["summary"]["broken"], 0)

    def test_inline_path_check_is_optional(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            file_path = self._write(
                root,
                ".instructions/a.md",
                "# A\n\nPath `org/roles/missing.md`\n",
            )
            result = validate_references(file_path, workspace_root=root, include_inline_paths=False)
            self.assertEqual(result["summary"]["broken"], 0)


if __name__ == "__main__":
    unittest.main()
