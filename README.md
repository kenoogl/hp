# Intelligent Modeling Laboratory (IML) Website Template

Hugo + Nginx + Docker で構築した、最小構成で保守しやすい研究室向け静的Webサイトテンプレートです。

## 構成

- `docker/docker-compose.yml`: 実行用コンテナ定義（ローカルビルド用）
- `docker/Dockerfile`: `public/` を Nginx イメージへ同梱
- `nginx/`: 追加のNginx設定ファイル置き場（将来拡張用）
- `site/`: Hugo ソース（テーマ、レイアウト、コンテンツ、静的アセット）
- `public/`: Hugo のビルド出力先

## ホームページ確認（推奨）

```bash
cd /Users/Daily/Development/HP/lab-website
make build
make up
```

ブラウザで [http://127.0.0.1](http://127.0.0.1) を開いて確認します。  
停止するときは `make down` を実行します。

## ローカルビルド（直接実行）

```bash
cd site
hugo --destination ../public
```

## デプロイ（直接実行）

```bash
cd docker
docker-compose up -d --build
```

その後、`http://127.0.0.1` を開いて確認します。

## コンテンツ更新フロー

1. `site/content/` 配下の Markdown を編集
2. `site/static/images/` 配下に画像を追加
3. Hugo を再ビルド
4. コンテナを再ビルドして再起動（`make up`）

## Publications メンテナンス方法

研究業績（Publications）は、次の3方式で更新できます。

### 1. 手動更新（Manual）

- 向いているケース: 論文数が少なく、更新頻度が低い場合
- 手順:
  1. `site/content/publications/<year>/` に Markdown を追加
  2. タイトル・著者・誌名・DOI・PDFリンク等を記載
  3. `make build && make up` で反映確認

### 2. 半自動更新（Semi-Automatic / BibTeX）

- 向いているケース: 安定運用しつつ、手作業を減らしたい場合
- 手順:
  1. `site/data/publications.bib` を更新（Scholar/Zotero/Scopus からエクスポート）
  2. 変換スクリプト `scripts/bibtex_to_markdown.py` を実行
  3. `make build && make up` で反映確認

### 3. 自動更新（Automatic）

- 向いているケース: 更新頻度が高く、運用を定常化したい場合
- 構成:
  1. BibTeX を定期取得
  2. 変換スクリプト実行
  3. 自動コミット
  4. サイト再ビルド
- 実装例: GitHub Actions の定期実行（weekly など）

詳細は [publications_workflow.md](/Users/Daily/Development/HP/lab-website/publications_workflow.md) を参照してください。

## セキュリティメモ

- 静的サイト専用構成（DB・アプリバックエンドなし）
- 生成済み `public/` をイメージに同梱して配信
- 必要に応じて `nginx/` 配下に独自設定を追加可能

## 将来の拡張案

- BibTeX からの出版リスト自動生成
- Google Scholar 連携
- News の RSS 配信
- Alumni アーカイブ自動化
- 研究可視化セクションの追加

## Makefile ショートカット

```bash
cd /Users/Daily/Development/HP/lab-website
make check   # 設定検証 + ビルド
make up      # nginx コンテナ起動
make ps      # コンテナ状態確認
make down    # コンテナ停止
```
