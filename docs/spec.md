# Laboratory Website System Specification

## 1. Purpose

本仕様は、研究室Webサイト運用システムの要件・構成・運用フローを定義する。  
対象システムは以下を満たす。

- 静的サイトとして安全かつ軽量に公開できること
- 論文情報を手動/半自動/自動で更新できること
- 継続的品質管理（軽量チェック + 月次監査）を自動実行できること
- 長期保守しやすい構成であること

---

## 2. Scope

対象リポジトリ: `lab-website`

含む範囲:
- Hugoコンテンツとテーマ
- Apache2公開設定
- Publications自動化（BibTeX -> Markdown）
- CI/CD（GitHub Actions）
- QAパイプライン（軽量チェック / 月次監査）

除外範囲:
- 動的バックエンド（DB, APIサーバ, PHP, WordPress）

---

## 3. System Architecture

### 3.1 Stack
- Static site generator: Hugo
- Web server (production): Apache2 on Ubuntu
- Source of truth: GitHub
- CI/CD: GitHub Actions
- Audit engine: Codex (monthly deep audit)
- Optional local runtime: Docker/Nginx

### 3.2 High-level flow
1. 編集者が `site/content` を更新
2. Hugoで `public/` を生成
3. CIで品質チェック
4. `develop` は staging、`main` は production へ配信
5. 月次でCodex監査レポートを生成

### 3.3 Directory contract
- `site/` : Hugo source
- `public/` : Hugo build output
- `data/` : Publications source data (`publications.bib`)
- `scripts/` : automation/validation scripts
- `.github/workflows/` : CI workflows
- `reports/` : monthly audit reports (generated)
- `apache/` : Apache VirtualHost / deploy-related configs
- `docker/`, `nginx/` : optional local verification configs

---

## 4. Functional Requirements

### 4.1 Site content management
- FR-001: コンテンツは `site/content/*` のMarkdownで管理する。
- FR-002: Hugo buildは `public/` に出力する。
- FR-003: build時は古い生成物を残さない（`--cleanDestinationDir`）。

### 4.2 Publication management
- FR-101: Publicationsは年別ディレクトリで管理する（`site/content/publications/<year>/`）。
- FR-102: BibTeXソースは `data/publications.bib` を単一ソースとする。
- FR-103: `scripts/bibtex_to_markdown.py` は BibTeX を Hugo Markdown に変換する。
- FR-104: `scripts/scholar_fetch.py` は Google Scholar から BibTeX を取得可能とする。
- FR-105: 各publicationに `pub_type` を保持し、`journal` / `international-conference` / `domestic-conference` / `others` の4分類表示を可能にする。

### 4.3 Validation and QA
- FR-201: `scripts/validate_content.py` は命名規約・Front Matter整合を検証する。
- FR-202: `scripts/check_markdown_validity.py` はMarkdown妥当性（UTF-8/Front Matter閉鎖）を検証する。
- FR-203: `scripts/check_internal_links.py` は生成HTML内の内部リンク切れを検出する。
- FR-204: 画像サイズ上限は 500KB とし、超過はCI失敗とする。

### 4.4 Deployment
- FR-301: Apache2は `public/` の静的ファイルのみを配信する。
- FR-302: production の `DocumentRoot` は `/var/www/html` を基準とする。
- FR-303: `develop` は staging、`main` は production へ GitHub Actions から rsync/scp で配信する。
- FR-304: サーバ側反映前に `apache2ctl configtest` を実行し、成功時のみ reload する。

### 4.5 CI/CD workflows
- FR-401: `update_publications.yml` は weekly で publication更新を実行する。
- FR-402: `site_checks.yml` は PR および develop/main push で軽量品質チェックを実行する。
- FR-403: `site_audit.yml` は monthly でフル監査を実行する。
- FR-404: 月次監査レポートは `reports/monthly_site_audit_YYYY-MM-DD.md` を出力する。

---

## 5. Non-Functional Requirements

### 5.1 Security
- NFR-SEC-001: 動的バックエンドを導入しない。
- NFR-SEC-002: Apache設定は `sites-available` 管理、`apache2ctl configtest` を必須化する。
- NFR-SEC-003: 秘密情報はリポジトリに保存せず GitHub Secrets を使用する。
- NFR-SEC-004: 本番サーバでの直接編集を禁止する。

### 5.2 Maintainability
- NFR-MNT-001: 命名規約を自動検証で強制する。
- NFR-MNT-002: ドキュメントは実装と同期する。
- NFR-MNT-003: 主要運用コマンドをMakefileに集約する。

### 5.3 Performance
- NFR-PERF-001: サイトは軽量静的配信を維持する。
- NFR-PERF-002: 画像サイズ上限 500KB を継続監視する。

### 5.4 Reliability
- NFR-REL-001: CI軽量チェックを通過しない変更は develop/main 品質基準を満たさない。
- NFR-REL-002: 月次監査で中長期的な構造劣化を検知する。

---

## 6. Content Conventions

### 6.1 Naming
- `site/content/research/*.md`: kebab-case
- `site/content/publications/<year>/*.md`: kebab-case

### 6.2 Publications metadata
各publicationページは以下を持つこと。
- `title`
- `date`
- `authors`
- `journal`（または同等のvenue）
- `year`
- `pub_type`（`journal` / `international-conference` / `domestic-conference` / `others`）
- `doi` または `doi_url`（推奨）

### 6.3 Year consistency
- publicationの `year` は所属ディレクトリ `<year>` と一致すること。
- `date` は `<year>-` で始まること。

---

## 7. Operational Workflows

### 7.1 Local development
1. `make check`
2. `cd site && hugo server`
3. ブラウザで `http://localhost:1313` を確認

### 7.2 Manual publication update
1. `site/content/publications/<year>/` にMarkdown追加
2. `make check`
3. PR経由で `develop` へ反映

### 7.3 Semi-automatic publication update
1. `data/publications.bib` 更新
2. `python scripts/bibtex_to_markdown.py data/publications.bib --clean`
3. `python scripts/validate_content.py`
4. `make check`

### 7.4 Fully automatic publication update
1. GitHub Actions (`update_publications.yml`) が定期実行
2. Scholar fetch -> BibTeX convert -> validation -> build
3. 変更があれば自動commit/push
4. `develop` 経由で staging 確認後、`main` で production 反映

### 7.5 Two-level QA pipeline
- Level 1: `site_checks.yml`（PR/develop/main）
- Level 2: `site_audit.yml`（monthly + manual）

---

## 8. CI Workflow Specifications

### 8.1 update_publications.yml
- Trigger: weekly schedule + manual dispatch
- Steps:
  - Python dependencies install
  - Scholar fetch（`SCHOLAR_AUTHOR_ID` 利用）
  - BibTeX->Markdown変換
  - content validation
  - Hugo build
  - commit/push

### 8.2 site_checks.yml
- Trigger: pull_request, push(develop/main)
- Checks:
  - content validation
  - Hugo build
  - markdown validity
  - internal links
  - image size threshold

### 8.3 site_audit.yml
- Trigger: monthly schedule + manual dispatch
- Steps:
  - baseline lightweight checks
  - Codex deep audit (`docs/lab_website_quality_audit.md` 指示)
  - report artifact upload
  - report commit/push
- Secret dependency:
  - `OPENAI_API_KEY`（未設定時はスキップ理由つきレポート生成）

---

## 9. Interfaces and Dependencies

### 9.1 Required tools
- Hugo (extended)
- Python 3.x
- rsync or scp (for deployment)
- Apache2 (Ubuntu production)

### 9.2 Python dependencies
- `scholarly`
- `bibtexparser`

### 9.3 GitHub secrets
- `SCHOLAR_AUTHOR_ID`（publication自動取得用）
- `OPENAI_API_KEY`（monthly Codex audit用）
- deployment credentials/secrets（SSH key, host, user）

---

## 10. Acceptance Criteria

- AC-001: `make check` が成功する。
- AC-002: `site_checks.yml` が develop/main/PR で成功する。
- AC-003: `update_publications.yml` が手動実行で成功する。
- AC-004: `site_audit.yml` が月次実行でレポートを生成する。
- AC-005: publicationページが年別/kebab-case規約を満たす。
- AC-006: 内部リンク切れが0件である。
- AC-007: `site/static/images` に 500KB 超過ファイルがない。

---

## 11. Out of Scope / Future Enhancements

- メンバー詳細スキーマ（写真・研究関心の必須化）
- HTML validator追加（QA強化）
- SEO拡張（OGP/Twitter/JSON-LD/canonical）
- Apache TLS/HSTS hardening

---

## 12. Reference Documents

- `README.md`
- `DEPLOY_CHECKLIST.md`
- `docs/publications_workflow.md`
- `docs/scholar_to_website_pipeline.md`
- `docs/lab_site_qa_pipeline.md`
- `docs/lab_website_quality_audit.md`
