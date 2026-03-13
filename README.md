# Intelligent Modeling Laboratory (IML) Website

Hugo で構築した研究室向け静的Webサイトです。  
本番公開は **Ubuntu + Apache2**、GitHub を唯一の正本として運用します。

## 運用方針

- GitHub を唯一の正本にする
- 本番サーバ（Ubuntu）で直接編集しない
- 変更は必ず PR / merge 経由で反映する
- 本番前にローカルまたは staging で確認する

## 構成

- `site/`: Hugo ソース（テーマ、レイアウト、コンテンツ、静的アセット）
- `public/`: Hugo のビルド出力（ローカル/CI生成物。Git 管理しない）
- `scripts/`: 自動化/検証スクリプト
- `data/`: BibTeX などのデータソース
- `.github/workflows/`: CI/CD
- `apache/`: Apache 本番設定（VirtualHost など）
- `docker/`, `nginx/`: ローカル検証向け（任意）

## ローカル確認（推奨）

```bash
cd /Users/Daily/Development/HP/lab-website
make build
make up
make ps
```

確認URL: [http://127.0.0.1](http://127.0.0.1)

停止:

```bash
cd /Users/Daily/Development/HP/lab-website
make down
```

## デプロイ方針（本番）

- `develop` への push: CIチェック + staging 配信
- `main` への push: CIチェック + production 配信
- 配信先は Ubuntu + Apache2（`/var/www/...`）
- 配信方式は `rsync`/`scp`（GitHub Actions 実行）
- `public/` は GitHub Actions 上でビルドし、配信用 artifact として扱う

## コンテンツ更新フロー

1. `site/content/` の Markdown を編集
2. `make build && make up && make ps` で確認
3. `feature/*` で commit / push
4. PR を `develop` へマージ
5. staging 確認後、`main` へマージ
6. production 反映

## 日英運用方針

- `Research`、`Members`、`Join`、主要な固定ページは日英対応を基本とする
- `News` は日本語のみで運用する
- 国際向けに告知したい重要ニュースのみ、必要に応じて個別に英語化する

## News 運用

- `1ニュース = 1 Markdown` として `site/content/news/` に保存する
- トップページでは最新5件を `日付 + 本文抜粋` で表示する
- `/news/` では年ごとの時系列アーカイブとして本文を表示する
- `title` は管理用メタデータとして保持し、トップページでは本文中心に見せる
- `date` はイベント開催日ではなく、ニュースを公開した日を入れる
- 未来日付を入れると Hugo の通常ビルドでは除外され、トップページや `/news/` に表示されない

詳細: [spec.md](/Users/Daily/Development/HP/lab-website/docs/specifications/spec.md)

## Publications メンテナンス

標準の更新方法は BibTeX ベースです。

```bash
cd /Users/Daily/Development/HP/lab-website
./scripts/update_publications.sh  # publication を更新してページ反映
```

- 手動更新・分類ルール・表示ルール: [publications_workflow.md](/Users/Daily/Development/HP/lab-website/docs/procedures/publications_workflow.md)
- Scholar 連携と自動更新: [scholar_to_website_pipeline.md](/Users/Daily/Development/HP/lab-website/docs/procedures/scholar_to_website_pipeline.md)
- 仕様上の要件: [spec.md](/Users/Daily/Development/HP/lab-website/docs/specifications/spec.md)

### `scholar_fetch.py` 利用法（ローカル）

プロジェクトルートで実行します。

```bash
cd /Users/Daily/Development/HP/lab-website
source .venv/bin/activate
```

基本例（著者ID指定）:

```bash
python scripts/scholar_fetch.py --author-id "kDMq7r4AAAAJ" --output data/publications.bib
```

著者名検索で取得する例:

```bash
python scripts/scholar_fetch.py --author-name "Kenji Ono" --output data/publications.bib
```

実運用例（年フィルタ・件数上限・リトライ付き）:

```bash
python scripts/scholar_fetch.py \
  --author-id "kDMq7r4AAAAJ" \
  --output data/publications.bib \
  --min-year 1990 \
  --max-pubs 200 \
  --retries 3 \
  --skip-errors \
  --verbose
```

取得後の更新フロー:

```bash
python scripts/bibtex_to_markdown.py data/publications.bib --clean
python scripts/validate_content.py
cd site && hugo --destination ../public --cleanDestinationDir
```

## QA パイプライン

- 軽量チェック: `.github/workflows/site_checks.yml`
  - Hugo build
  - Markdown validity
  - 内部リンク
  - 画像サイズ上限（500KB）
- 月次監査: `.github/workflows/site_audit.yml`
  - `reports/monthly_site_audit_YYYY-MM-DD.md` を生成
- 半年ごと監査（手動）
  - `audits/research_visibility_audit.md`
  - `audits/research_impact_audit.md`

監査用の LLM プロンプトは `docs/` ではなく `audits/` に分離して管理します。

詳細:
- [lab_site_qa_pipeline.md](/Users/Daily/Development/HP/lab-website/docs/operations/lab_site_qa_pipeline.md)
- [docs/README.md](/Users/Daily/Development/HP/lab-website/docs/README.md)

## 補足

リポジトリには `docker/` と `nginx/` がありますが、これは主にローカル検証用途です。  
本番配信は Ubuntu + Apache2 を基準に運用します。

## トラブルシュート（ローカル確認）

`make up` 実行時に以下のようなエラーが出る場合:

`failed to connect to the docker API at unix:///Users/.../.colima/default/docker.sock`

Colima（Dockerデーモン）が停止しています。以下で復旧します。

```bash
colima start
make up
make ps
```

`make ps` で `lab_web` が `Up` になっていれば、`http://127.0.0.1` で確認できます。
