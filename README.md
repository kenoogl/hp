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
