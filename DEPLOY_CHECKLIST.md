# デプロイチェックリスト

Intelligent Modeling Laboratory (IML) website template をデプロイする前の最終確認手順です。

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

以下を確認します。
- `build.context` が `..` である
- `dockerfile` が `docker/Dockerfile` である
- `image` が `lab-website-nginx:local` である

4. Dockerfile を確認

```bash
cat /Users/Daily/Development/HP/lab-website/docker/Dockerfile
```

`COPY public/ /usr/share/nginx/html/` が含まれることを確認します。

5. コンテナを起動

```bash
cd /Users/Daily/Development/HP/lab-website/docker
docker-compose up -d --build
```

6. 稼働状態を確認

```bash
docker-compose ps
```

`lab_web` のステータスが `Up` であることを確認します。

7. HTTP 応答を確認

```bash
curl -I http://127.0.0.1
```

`HTTP/1.1 200 OK` を含むことを確認します。

8. ブラウザ表示を確認

[http://127.0.0.1](http://127.0.0.1) を開き、次のナビゲーションが表示されることを確認します。
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
- `docker-compose up -d --build` を再実行
- ブラウザを再読み込みして更新が反映されることを確認
