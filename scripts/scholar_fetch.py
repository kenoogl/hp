#!/usr/bin/env python3
"""Fetch publications from Google Scholar and export a BibTeX file.

Usage:
  python scripts/scholar_fetch.py --author-id <SCHOLAR_ID>

The author id can also be provided via SCHOLAR_AUTHOR_ID environment variable.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from scholarly import scholarly


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Google Scholar publications to BibTeX")
    parser.add_argument("--author-id", default=os.getenv("SCHOLAR_AUTHOR_ID"), help="Google Scholar author id")
    parser.add_argument("--output", default="data/publications.bib", help="Output BibTeX file path")
    return parser.parse_args()


def _make_key(title: str, year: str) -> str:
    base = "".join(ch.lower() if ch.isalnum() else "_" for ch in title).strip("_")
    compact = "_".join(part for part in base.split("_") if part)
    short = compact[:60] if compact else "untitled"
    return f"{short}_{year}" if year else short


def _to_bibtex_entry(pub: dict) -> str:
    bib = pub.get("bib", {})
    title = bib.get("title", "").strip()
    authors = bib.get("author", "").strip()
    year = str(bib.get("pub_year", "")).strip()
    venue = bib.get("venue", "").strip()
    doi = str(pub.get("pub_url", "")).strip()

    key = _make_key(title, year)

    fields = [
        f"@article{{{key},",
        f"  title={{{title}}},",
        f"  author={{{authors}}},",
    ]
    if venue:
        fields.append(f"  journal={{{venue}}},")
    if year:
        fields.append(f"  year={{{year}}},")
    if doi:
        fields.append(f"  url={{{doi}}},")
    fields.append("}")
    return "\n".join(fields)


def main() -> int:
    args = parse_args()
    if not args.author_id:
        raise SystemExit("Missing author id. Set --author-id or SCHOLAR_AUTHOR_ID.")

    author = scholarly.search_author_id(args.author_id)
    author = scholarly.fill(author)

    entries: list[str] = []
    for pub in author.get("publications", []):
        pub = scholarly.fill(pub)
        entries.append(_to_bibtex_entry(pub))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n\n".join(entries) + "\n", encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
