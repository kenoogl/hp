# Publications Workflow

## Goal

Manage and update the Publications page of the laboratory website.

Two workflows must be supported:

1. Manual update
2. Automated update using BibTeX

The website uses:

- Hugo static site generator
- Markdown content
- Docker deployment

---

## Directory Structure

Current Hugo source root is `site/`.

```text
site/content/publications/
    2026/
    2025/
    2024/
```

Each publication is a markdown file.

---

## Method 1: Manual Publication Update

Best for:

- small labs
- low publication frequency

### Step 1

Create a new markdown file.

```text
site/content/publications/2026/wake-modeling.md
```

### Step 2

Insert metadata.

```yaml
---
title: "Data-driven Wake Modeling using AI"
authors: ["Kenji Ono", "John Smith"]
journal: "Journal of Wind Engineering"
year: 2026
doi: "10.xxxx/xxxxx"
pdf: "/pdf/wake2026.pdf"
---

Short description of the paper.
```

### Step 3

Rebuild site.

```bash
cd site
hugo --destination ../public
```

---

## Method 2: BibTeX Semi-Automatic Update

Use a single BibTeX file as source.

```text
data/publications.bib
```

Example entry:

```bibtex
@article{ono2026wake,
  title={Data-driven wake modeling using AI},
  author={Ono, Kenji and Smith, John},
  journal={Journal of Wind Engineering},
  year={2026},
  doi={10.xxxx/xxxxx}
}
```

BibTeX is a standard structured format for bibliographic data used widely in research publications.

### Step 1: Export BibTeX

Export publications from:

- Google Scholar
- Scopus
- Zotero

Save as:

```text
data/publications.bib
```

### Step 2: Run conversion script

Script reads BibTeX and generates markdown pages.

```text
scripts/bibtex_to_markdown.py
```

Example:

```bash
python scripts/bibtex_to_markdown.py data/publications.bib --clean
python scripts/validate_content.py
```

Output:

```text
site/content/publications/2026/paper_name.md
```

### Step 3: Build site

```bash
cd site
hugo --destination ../public
```

---

## Method 3: Fully Automatic Workflow

Goal:

Google Scholar -> website

Pipeline:

```text
Google Scholar
    ↓
BibTeX export
    ↓
Git repository
    ↓
Python converter
    ↓
Hugo build
    ↓
Website
```

---

## Optional Automation

Use GitHub Actions.

Workflow:

```yaml
schedule:
  weekly

steps:
  1 download scholar bibtex
  2 run converter script
  3 commit updates
  4 rebuild site
```

---

## Recommended Lab Workflow

For stability, use Method 2.

```text
Scholar
  ↓
BibTeX
  ↓
script
  ↓
site
```

Advantages:

- reproducible
- single source of truth
- easy maintenance
- compatible with LaTeX
