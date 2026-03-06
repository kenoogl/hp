# デプロイチェックリスト

AI for Science Laboratory website template をデプロイする前の最終確認手順です。

1. Hugo 出力を再ビルド

```bash
cd /Users/Daily/Development/HP/lab-website/site
hugo --destination ../public
```

2. 生成ファイルを確認

```bash
ls -la /Users/Daily/Development/HP/lab-website/public
```

`/Users/Daily/Development/HP/lab-website/public/index.html` が存在することを確認します。

3. Docker Compose 設定を確認

```bash
cat /Users/Daily/Development/HP/lab-website/docker/docker-compose.yml
```

次の2つが read-only (`:ro`) マウントであることを確認します。
- `../public:/usr/share/nginx/html:ro`
- `../nginx/nginx.conf:/etc/nginx/nginx.conf:ro`

4. Nginx 設定を確認

```bash
cat /Users/Daily/Development/HP/lab-website/nginx/nginx.conf
```

以下を確認します。
- `try_files $uri $uri/ =404;`
- セキュリティヘッダが設定されている
- `server_tokens off;`

5. コンテナを起動

```bash
cd /Users/Daily/Development/HP/lab-website/docker
docker compose up -d
```

6. 稼働状態を確認

```bash
docker compose ps
```

`lab_web` のステータスが `Up` であることを確認します。

7. HTTP 応答を確認

```bash
curl -I http://localhost
```

`HTTP/1.1 200 OK` を含むことを確認します。

8. ブラウザ表示を確認

[http://localhost](http://localhost) を開き、次のナビゲーションが表示されることを確認します。
- Home
- Research
- Publications
- Members
- Projects
- News
- Join Us
- Contact

9. コンテンツ更新スモークテスト

- `/Users/Daily/Development/HP/lab-website/site/content/news/2026-paper.md` を編集
- Hugo ビルドを再実行
- ブラウザを再読み込みして更新が反映されることを確認
