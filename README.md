# Intelligent Modeling Laboratory (IML) Website Template

Hugo + Nginx + Docker で構築した、最小構成で保守しやすい研究室向け静的Webサイトテンプレートです。

## 構成

- `docker/docker-compose.yml`: 実行用コンテナ定義
- `nginx/nginx.conf`: Nginx の静的配信設定
- `site/`: Hugo ソース（テーマ、レイアウト、コンテンツ、静的アセット）
- `public/`: Hugo のビルド出力先

## ローカルビルド

```bash
cd site
hugo --destination ../public
```

## デプロイ

```bash
cd docker
docker compose up -d
```

その後、`http://localhost` を開いて確認します。

## コンテンツ更新フロー

1. `site/content/` 配下の Markdown を編集
2. `site/static/images/` 配下に画像を追加
3. Hugo を再ビルド
4. Nginx が更新後の `public/` を配信

## セキュリティメモ

- 静的サイト専用構成（DB・アプリバックエンドなし）
- サイトコンテンツと Nginx 設定を read-only でマウント
- Nginx セキュリティヘッダを有効化
- `server_tokens off` によりバージョン情報露出を抑制

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
