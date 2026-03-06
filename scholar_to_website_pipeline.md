# Scholar to Website Pipeline

## Goal

Create a fully automated pipeline that updates the laboratory website publications page using Google Scholar data.

Pipeline:

Google Scholar -> BibTeX -> Markdown -> Hugo -> Website

The system must run automatically.

---

## System Architecture

Components:

1. Google Scholar (publication source)
2. BibTeX database
3. Python scripts
4. Hugo static site
5. Docker deployment

Pipeline:

```text
Scholar
  ↓
BibTeX
  ↓
Python conversion
  ↓
Markdown files
  ↓
Hugo build
  ↓
Website
```

---

## Repository Structure

```text
lab-website/

site/
  content/publications/
  data/publications.bib

scripts/
  fetch_scholar.py
  bibtex_to_markdown.py

.github/workflows/
  update_publications.yml
```

---

## Step 1: Fetch publications from Google Scholar

Use the Python library:

`scholarly`

Install:

```bash
pip install scholarly
```

Example script: `scripts/fetch_scholar.py`

```python
from pathlib import Path
from scholarly import scholarly

AUTHOR_ID = "YOUR_SCHOLAR_ID"

author = scholarly.search_author_id(AUTHOR_ID)
author = scholarly.fill(author)

bibtex_entries = []

for pub in author["publications"]:
    pub = scholarly.fill(pub)
    bib = pub["bib"]

    key = bib.get("title", "untitled").replace(" ", "_")

    entry = f"""@article{{{key},
  title={{{bib.get('title','')}}},
  author={{{bib.get('author','')}}},
  year={{{bib.get('pub_year','')}}},
  journal={{{bib.get('venue','')}}}
}}"""

    bibtex_entries.append(entry)

Path("site/data").mkdir(parents=True, exist_ok=True)
Path("site/data/publications.bib").write_text("\n\n".join(bibtex_entries), encoding="utf-8")
```

This script generates:

`site/data/publications.bib`

---

## Step 2: Convert BibTeX to Hugo markdown

Script: `scripts/bibtex_to_markdown.py`

```python
from pathlib import Path
import bibtexparser

with open("site/data/publications.bib", encoding="utf-8") as bibfile:
    db = bibtexparser.load(bibfile)

out_dir = Path("site/content/publications")
out_dir.mkdir(parents=True, exist_ok=True)

for entry in db.entries:
    title = entry.get("title", "")
    authors = entry.get("author", "")
    year = entry.get("year", "")
    journal = entry.get("journal", "")

    filename = title.replace(" ", "_")[:50] or "untitled"

    md = f"""---
title: \"{title}\"
authors: \"{authors}\"
journal: \"{journal}\"
year: \"{year}\"
---

"""

    path = out_dir / f"{filename}.md"
    path.write_text(md, encoding="utf-8")
```

Output example:

`site/content/publications/wake_modeling.md`

---

## Step 3: Hugo build

Run:

```bash
cd site
hugo --destination ../public
```

Output:

`public/`

---

## Step 4: Docker deployment

```bash
make up
```

Website becomes available:

`http://127.0.0.1`

---

## Step 5: GitHub Actions automation

`.github/workflows/update_publications.yml`

```yaml
name: update publications

on:
  schedule:
    - cron: "0 2 * * 0"
  workflow_dispatch:

jobs:
  update:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: setup python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: install dependencies
        run: pip install scholarly bibtexparser

      - name: fetch scholar
        run: python scripts/fetch_scholar.py

      - name: convert bibtex
        run: python scripts/bibtex_to_markdown.py

      - name: build hugo output
        run: |
          cd site
          hugo --destination ../public

      - name: commit and push
        run: |
          git config user.name github-actions
          git config user.email actions@github.com
          git add .
          git commit -m "update publications" || echo "No changes to commit"
          git push
```

---

## Workflow Summary

Every week:

1. Fetch publications from Scholar
2. Generate BibTeX
3. Convert to Markdown
4. Build Hugo output
5. Commit and deploy updates

---

## Advantages

Automatic publication update:

```text
Scholar updated
  ↓
Website updated
```

Reduced manual work.

---

## Optional Improvements

Add:

- DOI extraction
- PDF links
- Citation counts
- Research topics
