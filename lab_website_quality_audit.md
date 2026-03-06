# Laboratory Website Quality Audit

Date: 2026-03-06  
Repository: `/Users/Daily/Development/HP/lab-website`

## 1. Site architecture summary

The repository follows a static site architecture and matches the intended stack:
- Hugo site source and theme layouts
- Nginx static serving
- Docker-based deployment

Validated components:
- Hugo config: `site/config.toml`
- Nginx config: `nginx/nginx.conf`
- Container build/runtime: `docker/Dockerfile`, `docker/docker-compose.yml`

No dynamic backend patterns were detected:
- No PHP files
- No DB config/dependency files
- No WordPress traces

## 2. Strengths

- Static architecture is clean and production-appropriate for academic lab websites.
- Required top-level directories exist: `docker/`, `nginx/`, `site/`, `data/`, `scripts/`, `public/`.
- Publication automation is in place:
  - `data/publications.bib`
  - `scripts/scholar_fetch.py`
  - `scripts/bibtex_to_markdown.py`
  - `.github/workflows/update_publications.yml`
- Content convention validation exists and is wired into local checks and CI:
  - `scripts/validate_content.py`
  - `Makefile` (`lint-content`, `check`)
- Security baseline is reasonable for static serving (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `server_tokens off`).
- Performance baseline is strong:
  - very small HTML pages
  - SVG assets only, all far below 500KB
  - no runtime JavaScript payload

## 3. Weaknesses

- Main navigation is too wide for the stated UX guideline (8 items vs recommended max 6).
- Members section lacks expected academic profile detail fields:
  - no per-person pages
  - no photos
  - no role/position metadata schema
  - no research interests metadata
- SEO is minimal:
  - site-wide description reused on all pages
  - no canonical link
  - no Open Graph/Twitter metadata
  - no structured data (JSON-LD)
- Heading hierarchy is shallow on many pages (only `h1`, no supporting `h2` sections).
- Taxonomy pages (`/tags`, `/categories`) are generated but not integrated into navigation, creating orphan-like endpoints.

## 4. Missing features

- Structured member profile model in content and templates.
- Enhanced homepage research communication blocks (featured projects / publication cards with DOI/PDF actions).
- SEO metadata layer at template level.
- Accessibility refinements beyond baseline semantics (landmark/heading depth consistency, richer link context).
- Optional hardening headers (CSP, Permissions-Policy, HSTS under TLS).

## 5. Recommended improvements

1. Reduce top navigation to <=6 primary items; move secondary links to footer.
2. Redesign members content model:
   - one file per person
   - front matter keys: `name`, `position`, `email`, `interests`, `photo`
3. Add SEO template partials in base layout:
   - canonical
   - Open Graph
   - Twitter cards
   - JSON-LD for organization/publications
4. Improve heading hierarchy in list/single templates by introducing meaningful `h2` section headings.
5. Resolve taxonomy behavior:
   - disable if unused, or
   - expose via navigation/filter UI.
6. Add security header hardening where deployment environment allows it.
7. Add optional QA checks (HTML/link validation) in CI.

## 6. Priority fixes

### Critical

- None identified in current static architecture.

### Recommended

1. Navigation simplification (8 -> <=6 items).
2. Members information model upgrade.
3. SEO metadata implementation in base template.
4. Heading hierarchy improvements across major pages.
5. Taxonomy orphan resolution.

### Optional

1. CSP/HSTS/Permissions-Policy enhancement.
2. Font delivery optimization (self-hosting / fallback strategy).
3. Add link checker + HTML validation to CI quality gate.

---

## Ticket-ready implementation backlog

### Recommended

- [ ] NAV-001: Reduce primary menu to max 6 items and move secondary links to footer.
- [ ] MEM-001: Create member profile schema and migrate content to one-page-per-person format.
- [ ] SEO-001: Add canonical, Open Graph, Twitter card metadata in `baseof.html`.
- [ ] SEO-002: Add JSON-LD organization schema and publication schema where applicable.
- [ ] IA-001: Introduce `h2` section structure in list/single templates.
- [ ] IA-002: Disable or integrate taxonomy pages (`tags`, `categories`).

### Optional

- [ ] SEC-001: Add CSP and Permissions-Policy headers in `nginx.conf`.
- [ ] SEC-002: Add HSTS header after TLS termination policy is defined.
- [ ] PERF-001: Evaluate self-hosted fonts vs Google Fonts dependency.
- [ ] QA-001: Add HTML and link validation job in GitHub Actions.
