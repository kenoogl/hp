#!/usr/bin/env python3
"""Convert BibTeX entries into Hugo publication markdown files.

Input:  data/publications.bib
Output: site/content/publications/<year>/<slug>.md
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import bibtexparser


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert BibTeX to Hugo markdown")
    parser.add_argument("bib", nargs="?", default="data/publications.bib", help="BibTeX input path")
    parser.add_argument(
        "--output-dir",
        default="site/content/publications",
        help="Hugo publications content root",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove generated publication files before writing new ones",
    )
    return parser.parse_args()


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return slug[:80] if slug else "untitled"


def get_venue(entry: dict) -> str:
    return entry.get("journal") or entry.get("booktitle") or entry.get("publisher") or ""


def parse_year(entry: dict) -> str:
    year = str(entry.get("year", "")).strip()
    return year if year.isdigit() else "unknown"


def detect_pub_type(entry: dict) -> str:
    entry_type = str(entry.get("ENTRYTYPE", "")).strip().lower()
    venue = get_venue(entry).lower()
    if entry_type == "article":
        return "journal"
    if entry_type in {"inproceedings", "conference", "proceedings"}:
        return "international-conference"
    if "conference" in venue or "symposium" in venue or "workshop" in venue:
        return "international-conference"
    return "others"


def build_markdown(entry: dict) -> str:
    title = entry.get("title", "").replace("\n", " ").strip()
    authors = entry.get("author", "").replace("\n", " ").strip()
    venue = get_venue(entry).replace("\n", " ").strip() or "Unknown venue"
    year = parse_year(entry)
    pub_type = detect_pub_type(entry)
    doi = entry.get("doi", "").strip()
    url = entry.get("url", "").strip()

    date = f"{year}-01-01" if year.isdigit() else "1970-01-01"

    lines = [
        "---",
        f'title: "{title}"',
        f'date: {date}',
        f'authors: "{authors}"',
        f'journal: "{venue}"',
        f'year: "{year}"',
        f'pub_type: "{pub_type}"',
    ]
    if doi:
        lines.append(f'doi: "{doi}"')
    if url:
        lines.append(f'doi_url: "{url}"')
    lines.extend(["---", "", f"{title}."])
    return "\n".join(lines) + "\n"


def clean_generated_files(root: Path) -> None:
    for year_dir in root.iterdir():
        if not year_dir.is_dir():
            continue
        for path in year_dir.glob("*.md"):
            if path.name == "_index.md":
                continue
            path.unlink()


def main() -> int:
    args = parse_args()
    bib_path = Path(args.bib)
    out_root = Path(args.output_dir)

    if not bib_path.exists():
        raise SystemExit(f"BibTeX file not found: {bib_path}")

    with bib_path.open(encoding="utf-8") as bibfile:
        db = bibtexparser.load(bibfile)

    out_root.mkdir(parents=True, exist_ok=True)
    if args.clean:
        clean_generated_files(out_root)

    written = 0
    for entry in db.entries:
        title = entry.get("title", "").strip()
        if not title:
            continue

        year = parse_year(entry)
        year_dir = out_root / year
        year_dir.mkdir(parents=True, exist_ok=True)

        slug = slugify(title)
        md_path = year_dir / f"{slug}.md"
        md_path.write_text(build_markdown(entry), encoding="utf-8")
        written += 1

    print(f"Generated {written} publication markdown files under {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
