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
    if not slug:
        return "untitled"
    return slug[:80].strip("-") or "untitled"


def yaml_quote(value: str) -> str:
    # Use single-quoted YAML scalars and escape embedded single quotes.
    return "'" + value.replace("'", "''") + "'"


def get_venue(entry: dict) -> str:
    return entry.get("journal") or entry.get("booktitle") or entry.get("publisher") or ""


def parse_year(entry: dict) -> str:
    # Prefer explicit year-like fields.
    for key in ("year", "pub_year", "date"):
        raw = str(entry.get(key, "")).strip()
        if raw.isdigit() and len(raw) == 4:
            return raw
        m = re.search(r"(19|20)\d{2}", raw)
        if m:
            return m.group(0)

    # Fallback: infer year from venue/note text when possible.
    fallback_blob = " ".join(
        [
            str(entry.get("journal", "")),
            str(entry.get("booktitle", "")),
            str(entry.get("note", "")),
        ]
    )
    m = re.search(r"(19|20)\d{2}", fallback_blob)
    if m:
        return m.group(0)

    return "unknown"


def _is_domestic_conference_venue(venue: str) -> bool:
    v = (venue or "").lower()
    if not v:
        return False

    if "international" in v:
        return False

    domestic_keywords = [
        "情報処理学会",
        "電子情報通信学会",
        "日本機械学会",
        "日本計算工学会",
        "可視化情報学会",
        "日本流体力学会",
        "全国大会",
        "年次大会",
        "講演会",
        "研究会",
        "ipsj",
        "ieice",
    ]
    return any(k in v for k in domestic_keywords)


def _contains_japanese(text: str) -> bool:
    if not text:
        return False
    return bool(re.search(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff]", text))


def _normalize_pub_type(value: str) -> str:
    v = (value or "").strip().lower().replace("_", "-")
    allowed = {"journal", "international-conference", "domestic-conference", "others", "talk"}
    return v if v in allowed else ""


def _parse_boolish(value: str) -> bool | None:
    v = (value or "").strip().lower()
    if v in {"true", "yes", "y", "1", "reviewed", "refereed", "peer-reviewed", "査読あり", "査読有"}:
        return True
    if v in {"false", "no", "n", "0", "non-refereed", "nonrefereed", "unreviewed", "査読なし", "査読無"}:
        return False
    return None


def detect_pub_type(entry: dict) -> str:
    manual_type = _normalize_pub_type(str(entry.get("pub_type", "")))
    if manual_type:
        return manual_type

    entry_type = str(entry.get("ENTRYTYPE", "")).strip().lower()
    venue = get_venue(entry)
    authors = str(entry.get("author", "")).strip()

    # Heuristic requested by operation policy:
    # if venue (journal/booktitle) or author string contains Japanese,
    # classify as domestic conference.
    if _contains_japanese(venue) or _contains_japanese(authors):
        return "domestic-conference"

    if entry_type == "article":
        return "journal"
    if entry_type in {"inproceedings", "conference", "proceedings"}:
        if _is_domestic_conference_venue(venue):
            return "domestic-conference"
        return "international-conference"
    venue_lower = venue.lower()
    if "conference" in venue_lower or "symposium" in venue_lower or "workshop" in venue_lower:
        if _is_domestic_conference_venue(venue):
            return "domestic-conference"
        return "international-conference"
    return "others"


def detect_peer_reviewed(entry: dict, bib_path: Path, pub_type: str) -> bool | None:
    if pub_type not in {"international-conference", "domestic-conference"}:
        return None

    for key in ("peer_reviewed", "peerreviewed", "refereed", "reviewed"):
        manual = _parse_boolish(str(entry.get(key, "")))
        if manual is not None:
            return manual

    blob = " ".join(
        [
            str(entry.get("note", "")),
            str(entry.get("keywords", "")),
            str(entry.get("booktitle", "")),
            str(entry.get("journal", "")),
            str(entry.get("howpublished", "")),
        ]
    ).lower()
    if any(k in blob for k in ("non-refereed", "non refereed", "査読なし", "without review", "wip")):
        return False
    if any(k in blob for k in ("peer-reviewed", "peer reviewed", "refereed", "査読あり", "査読付")):
        return True

    stem = bib_path.stem.lower()
    if "non_refereed" in stem or "non-refereed" in stem:
        return False
    if "refereed" in stem and "non_refereed" not in stem and "non-refereed" not in stem:
        return True

    return None


def build_markdown(entry: dict, bib_path: Path) -> str:
    title = entry.get("title", "").replace("\n", " ").strip()
    authors = entry.get("author", "").replace("\n", " ").strip()
    venue = get_venue(entry).replace("\n", " ").strip() or "Unknown venue"
    year = parse_year(entry)
    pub_type = detect_pub_type(entry)
    peer_reviewed = detect_peer_reviewed(entry, bib_path, pub_type)
    doi = entry.get("doi", "").strip()
    url = entry.get("url", "").strip()
    annote = str(entry.get("annote", "") or entry.get("annotation", "")).strip()
    abstract = str(entry.get("abstract", "")).strip()
    if abstract:
        abstract = re.sub(r"\s+", " ", abstract)

    date = f"{year}-01-01" if year.isdigit() else "1970-01-01"

    lines = [
        "---",
        f"title: {yaml_quote(title)}",
        f'date: {date}',
        f"authors: {yaml_quote(authors)}",
        f"journal: {yaml_quote(venue)}",
        f"year: {yaml_quote(year)}",
        f"pub_type: {yaml_quote(pub_type)}",
    ]
    if peer_reviewed is not None:
        lines.append(f"peer_reviewed: {'true' if peer_reviewed else 'false'}")
    if annote:
        lines.append(f"annote: {yaml_quote(annote)}")
    if doi:
        lines.append(f"doi: {yaml_quote(doi)}")
    if url:
        lines.append(f"doi_url: {yaml_quote(url)}")
    if abstract:
        lines.append(f"abstract: {yaml_quote(abstract)}")
    lines.extend(["---", ""])
    return "\n".join(lines) + "\n"


def clean_generated_files(root: Path) -> None:
    for year_dir in root.iterdir():
        if not year_dir.is_dir():
            continue
        for path in year_dir.glob("*.md"):
            if path.name == "_index.md":
                continue
            path.unlink()


def resolve_unique_md_path(year_dir: Path, slug: str) -> Path:
    base = year_dir / f"{slug}.md"
    if not base.exists():
        return base

    n = 2
    while True:
        candidate = year_dir / f"{slug}-{n}.md"
        if not candidate.exists():
            return candidate
        n += 1


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
        md_path = resolve_unique_md_path(year_dir, slug)
        md_path.write_text(build_markdown(entry, bib_path), encoding="utf-8")
        written += 1

    print(f"Generated {written} publication markdown files under {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
