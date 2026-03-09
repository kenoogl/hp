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
- `public/`: Hugo のビルド出力
- `scripts/`: 自動化/検証スクリプト
- `data/`: BibTeX などのデータソース
- `.github/workflows/`: CI/CD
- `apache/`: Apache 本番設定（VirtualHost など）
- `docker/`, `nginx/`: ローカル検証向け（任意）

## ローカル開発

```bash
cd /Users/Daily/Development/HP/lab-website/site
hugo server
```

確認URL: [http://localhost:1313](http://localhost:1313)

## 本番用ビルド

```bash
cd /Users/Daily/Development/HP/lab-website/site
hugo --destination ../public --cleanDestinationDir
```

## デプロイ方針（本番）

- `develop` への push: CIチェック + staging 配信
- `main` への push: CIチェック + production 配信
- 配信先は Ubuntu + Apache2（`/var/www/...`）
- 配信方式は `rsync`/`scp`（GitHub Actions 実行）

## コンテンツ更新フロー

1. `site/content/` の Markdown を編集
2. `hugo server` で確認
3. `feature/*` で commit / push
4. PR を `develop` へマージ
5. staging 確認後、`main` へマージ
6. production 反映

## Publications メンテナンス

### 手動

- `site/content/publications/<year>/` に Markdown を追加
- `hugo --destination ../public --cleanDestinationDir` で確認

### 半自動（BibTeX）

```bash
python scripts/bibtex_to_markdown.py data/publications.bib --clean
python scripts/validate_content.py
```

### 自動

- `.github/workflows/update_publications.yml` を weekly 実行
- Scholar/BibTeX から更新 → Markdown 生成 → CI 検証

詳細: [publications_workflow.md](/Users/Daily/Development/HP/lab-website/docs/publications_workflow.md)

## QA パイプライン

- 軽量チェック: `.github/workflows/site_checks.yml`
  - Hugo build
  - Markdown validity
  - 内部リンク
  - 画像サイズ上限（500KB）
- 月次監査: `.github/workflows/site_audit.yml`
  - `reports/monthly_site_audit_YYYY-MM-DD.md` を生成
- 半年ごと監査（手動）
  - `docs/research_visibility_audit.md`
  - `docs/research_impact_audit.md`

詳細: [lab_site_qa_pipeline.md](/Users/Daily/Development/HP/lab-website/docs/lab_site_qa_pipeline.md)

## 補足

リポジトリには `docker/` と `nginx/` がありますが、これは主にローカル検証用途です。  
本番配信は Ubuntu + Apache2 を基準に運用します。
