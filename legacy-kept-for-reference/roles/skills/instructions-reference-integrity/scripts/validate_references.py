#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^```")
INLINE_PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+\.[A-Za-z0-9]+|[A-Za-z0-9_./-]+/[A-Za-z0-9_./-]+)`")
IGNORE_INLINE_TOKENS = {"path", "target", "scope"}


def _slugify(heading: str) -> str:
    text = heading.strip().lower()
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"[^a-z0-9\-\s]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def _iter_md_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.suffix.lower() == ".md" else []
    if target.is_dir():
        return sorted(p for p in target.rglob("*.md") if p.is_file())
    return []


def _extract_anchors(file_path: Path) -> set[str]:
    in_fence = False
    values: set[str] = set()
    for line in file_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            values.add(_slugify(match.group(2)))
    return values


def _is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:"))


def _split_target(target: str) -> tuple[str, str]:
    if "#" in target:
        part, frag = target.split("#", 1)
        return part.strip(), frag.strip()
    return target.strip(), ""


def _record(findings: list[dict], file_path: Path, line: int, target: str, code: str, detail: str):
    findings.append(
        {
            "file": str(file_path),
            "line": line,
            "target": target,
            "code": code,
            "detail": detail,
        }
    )


def _inline_path_exists(raw: str, file_path: Path, workspace_root: Path) -> bool:
    instructions_root = workspace_root / ".instructions"
    candidates = [
        (file_path.parent / raw).resolve(),
        (workspace_root / raw).resolve(),
        (instructions_root / raw).resolve(),
    ]
    return any(candidate.exists() for candidate in candidates)


def validate_references(target: Path, workspace_root: Path, include_inline_paths: bool = True) -> dict:
    files = _iter_md_files(target)
    anchor_index: dict[Path, set[str]] = {}

    def anchors_for(path: Path) -> set[str]:
        resolved = path.resolve()
        if resolved not in anchor_index:
            if resolved.exists() and resolved.is_file() and resolved.suffix.lower() == ".md":
                anchor_index[resolved] = _extract_anchors(resolved)
            else:
                anchor_index[resolved] = set()
        return anchor_index[resolved]

    findings: list[dict] = []
    links_checked = 0
    inline_checked = 0

    for file_path in files:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        in_fence = False

        for line_no, line in enumerate(lines, start=1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            for match in LINK_RE.finditer(line):
                link_target = match.group(1).strip()
                if not link_target or _is_external(link_target):
                    continue

                links_checked += 1

                if link_target.startswith("#"):
                    fragment = link_target[1:]
                    if fragment and fragment not in anchors_for(file_path):
                        _record(
                            findings,
                            file_path,
                            line_no,
                            link_target,
                            "ANCHOR_NOT_FOUND",
                            "In-file anchor does not exist",
                        )
                    continue

                path_part, fragment = _split_target(link_target)
                resolved = (file_path.parent / path_part).resolve()
                if not resolved.exists():
                    _record(
                        findings,
                        file_path,
                        line_no,
                        link_target,
                        "FILE_NOT_FOUND",
                        "Link target path does not exist",
                    )
                    continue

                if fragment and resolved.suffix.lower() == ".md":
                    target_anchors = anchors_for(resolved)
                    if fragment not in target_anchors:
                        _record(
                            findings,
                            file_path,
                            line_no,
                            link_target,
                            "ANCHOR_NOT_FOUND",
                            "Anchor fragment not found in target markdown",
                        )

            if include_inline_paths:
                for match in INLINE_PATH_RE.finditer(line):
                    raw = match.group(1)
                    if raw in IGNORE_INLINE_TOKENS:
                        continue
                    if raw.startswith(("http://", "https://")):
                        continue
                    inline_checked += 1
                    if _inline_path_exists(raw=raw, file_path=file_path, workspace_root=workspace_root):
                        continue
                    _record(
                        findings,
                        file_path,
                        line_no,
                        raw,
                        "INLINE_PATH_NOT_FOUND",
                        "Inline path-like reference does not resolve",
                    )

    summary = {
        "files_scanned": len(files),
        "links_checked": links_checked,
        "inline_paths_checked": inline_checked,
        "broken": len(findings),
    }

    return {
        "scope": str(target),
        "summary": summary,
        "findings": findings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate markdown reference integrity")
    parser.add_argument("target", nargs="?", default=".instructions", help="File or directory to scan")
    parser.add_argument(
        "--workspace-root",
        default=".",
        help="Workspace root used for resolving root-relative inline references",
    )
    parser.add_argument(
        "--no-inline-paths",
        action="store_true",
        help="Disable inline path-like reference checks",
    )
    args = parser.parse_args()

    target = Path(args.target).resolve()
    workspace_root = Path(args.workspace_root).resolve()

    result = validate_references(
        target=target,
        workspace_root=workspace_root,
        include_inline_paths=not args.no_inline_paths,
    )
    print(json.dumps(result, indent=2))

    return 1 if result["summary"]["broken"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
