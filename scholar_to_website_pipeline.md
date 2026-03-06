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

data/
  publications.bib

scripts/
  scholar_fetch.py
  bibtex_to_markdown.py
  validate_content.py

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

Run:

```bash
pip install scholarly
python scripts/scholar_fetch.py --author-id "<YOUR_SCHOLAR_ID>" --output data/publications.bib
```

Output:

`data/publications.bib`

---

## Step 2: Convert BibTeX to Hugo markdown

Run:

```bash
pip install bibtexparser
python scripts/bibtex_to_markdown.py data/publications.bib --clean
python scripts/validate_content.py
```

Output example:

`site/content/publications/2026/wake-modeling.md`

---

## Step 3: Hugo build

Run:

```bash
cd site
hugo --destination ../public --cleanDestinationDir
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
        env:
          SCHOLAR_AUTHOR_ID: ${{ secrets.SCHOLAR_AUTHOR_ID }}
        run: |
          if [ -z "$SCHOLAR_AUTHOR_ID" ]; then
            echo "SCHOLAR_AUTHOR_ID is not set; skipping fetch step."
          else
            python scripts/scholar_fetch.py --author-id "$SCHOLAR_AUTHOR_ID" --output data/publications.bib
          fi

      - name: convert bibtex
        run: python scripts/bibtex_to_markdown.py data/publications.bib --clean

      - name: validate content conventions
        run: python scripts/validate_content.py

      - name: build hugo output
        run: |
          cd site
          hugo --destination ../public --cleanDestinationDir

      - name: commit and push
        run: |
          git config user.name github-actions
          git config user.email actions@github.com
          git add data/publications.bib site/content/publications public
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
