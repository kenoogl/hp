#!/usr/bin/env python3
"""Validate Hugo content naming and front matter conventions.

Checks:
- research/*.md filenames are kebab-case (except _index.md)
- publications/<year>/*.md filenames are kebab-case (except _index.md)
- required front matter keys exist
- publication year/date are consistent with directory year
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DIR = ROOT / "site" / "content" / "research"
PUBLICATIONS_DIR = ROOT / "site" / "content" / "publications"

KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
YEAR_DIR_RE = re.compile(r"^\d{4}$")
PUB_TYPES = {"journal", "international-conference", "others"}


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("missing YAML front matter")

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ValueError("unterminated YAML front matter")

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.strip().startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def is_kebab_md(name: str) -> bool:
    return bool(KEBAB_RE.fullmatch(name))


def validate_research(errors: list[str]) -> None:
    for path in sorted(RESEARCH_DIR.glob("*.md")):
        if path.name == "_index.md":
            continue
        if not is_kebab_md(path.name):
            errors.append(f"[research] filename must be kebab-case: {path}")
        try:
            fm = parse_front_matter(path)
        except ValueError as exc:
            errors.append(f"[research] {path}: {exc}")
            continue
        for key in ("title", "date", "summary"):
            if not fm.get(key):
                errors.append(f"[research] {path}: missing front matter key '{key}'")


def validate_publications(errors: list[str]) -> None:
    for year_dir in sorted(PUBLICATIONS_DIR.iterdir()):
        if not year_dir.is_dir():
            continue
        if not YEAR_DIR_RE.fullmatch(year_dir.name):
            errors.append(f"[publications] year directory must be YYYY: {year_dir}")
            continue

        for path in sorted(year_dir.glob("*.md")):
            if path.name == "_index.md":
                continue
            if not is_kebab_md(path.name):
                errors.append(f"[publications] filename must be kebab-case: {path}")

            try:
                fm = parse_front_matter(path)
            except ValueError as exc:
                errors.append(f"[publications] {path}: {exc}")
                continue

            for key in ("title", "date", "authors", "journal", "year", "pub_type"):
                if not fm.get(key):
                    errors.append(f"[publications] {path}: missing front matter key '{key}'")

            if fm.get("year") and fm["year"] != year_dir.name:
                errors.append(
                    f"[publications] {path}: year '{fm['year']}' does not match directory '{year_dir.name}'"
                )

            if fm.get("date") and not fm["date"].startswith(f"{year_dir.name}-"):
                errors.append(
                    f"[publications] {path}: date '{fm['date']}' should start with '{year_dir.name}-'"
                )

            if fm.get("pub_type") and fm["pub_type"] not in PUB_TYPES:
                errors.append(
                    f"[publications] {path}: pub_type '{fm['pub_type']}' must be one of {sorted(PUB_TYPES)}"
                )


def main() -> int:
    errors: list[str] = []

    if not RESEARCH_DIR.exists():
        errors.append(f"Missing research directory: {RESEARCH_DIR}")
    if not PUBLICATIONS_DIR.exists():
        errors.append(f"Missing publications directory: {PUBLICATIONS_DIR}")

    if not errors:
        validate_research(errors)
        validate_publications(errors)

    if errors:
        print("Content validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
