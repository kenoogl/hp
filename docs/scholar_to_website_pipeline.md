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
5. GitHub Actions deploy to Ubuntu + Apache2

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
Deploy public/ to Ubuntu Apache2
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

## Step 4: Deploy to Ubuntu + Apache2

Deploy generated static files to server:

```text
GitHub Actions -> rsync/scp -> /var/www/mercury-staging (develop)
GitHub Actions -> rsync/scp -> /var/www/html (main)
```

Website URLs:
- Staging: `http://staging.mercury.cc.kyushu-u.ac.jp`
- Production: `http://mercury.cc.kyushu-u.ac.jp`

---

## Step 5: GitHub Actions automation

`.github/workflows/update_publications.yml`

Core behavior:

1. Install Python deps (`scholarly`, `bibtexparser`)
2. Fetch Scholar data (`SCHOLAR_AUTHOR_ID`)
3. Convert BibTeX to Markdown
4. Validate content conventions
5. Build Hugo output
6. Commit and push publication updates

---

## Step 6: Quality gates

After publication sync, quality checks run via:

- `.github/workflows/site_checks.yml`
  - Hugo build
  - content validation
  - markdown validity
  - internal link checks
  - image size threshold (500KB)
- `.github/workflows/site_audit.yml`
  - monthly full audit report
  - Codex-based deep review using `docs/lab_website_quality_audit.md`

---

## Workflow Summary

Every week:

1. Fetch publications from Scholar
2. Generate BibTeX
3. Convert to Markdown
4. Validate content and build Hugo output
5. Commit updates
6. Deploy via branch policy (`develop`/`main`)

---

## Advantages

Automatic publication update:

```text
Scholar updated
  ↓
Website updated
```

Reduced manual work while preserving staging review safety.

---

## Optional Improvements

Add:

- DOI extraction hardening
- PDF links
- Citation counts
- Research topic tags
