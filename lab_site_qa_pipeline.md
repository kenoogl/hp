# Lab Site QA Pipeline

## Goal

Implement a two-level quality monitoring system for the laboratory website.

Levels:
1. Lightweight automatic checks
2. Periodic full site audit

The system runs automatically using GitHub Actions, with Codex used for monthly deep audits.

---

## System Overview

Developer commit
↓
CI lightweight checks
↓
Site build validation
↓
Monthly Codex audit
↓
Quality report

---

## Level 1: Lightweight Automatic Checks

Workflow file:
- `.github/workflows/site_checks.yml`

Trigger:
- On every pull request
- On push to `main`

Checks:
- Hugo build success
- Broken internal links (`public/` HTML)
- Image size threshold (`site/static/images`, 500KB max)
- Markdown validity
- Content naming/front matter conventions

Implementation scripts:
- `scripts/check_internal_links.py`
- `scripts/check_markdown_validity.py`
- `scripts/validate_content.py`

---

## Level 2: Monthly Full Audit

Workflow file:
- `.github/workflows/site_audit.yml`

Trigger:
- Monthly schedule (`0 3 1 * *`, UTC)
- Manual dispatch

Flow:
1. Run baseline lightweight checks
2. Execute Codex audit prompt based on `lab_website_quality_audit.md`
3. Save report to `reports/monthly_site_audit_YYYY-MM-DD.md`
4. Upload report artifact
5. Commit report back to `main`

Codex prompt:
- "Read the repository and execute the instructions in `lab_website_quality_audit.md`. Output a full audit report in markdown."

Requirements:
- GitHub secret `OPENAI_API_KEY` must be configured for Codex execution.
- If secret or CLI is unavailable, workflow writes a fallback report explaining the skip reason.

---

## Priority Levels for Findings

- critical
- recommended
- optional

---

## Typical Lab Maintenance Flow

paper accepted
↓
Google Scholar update
↓
publication automation
↓
site update
↓
CI checks
↓
monthly full audit

---

## Benefits

- Site reliability
- Consistent structure
- Automatic error detection
- Long-term maintainability
