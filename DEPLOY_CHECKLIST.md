# Deploy Checklist

Final pre-deployment checks for the AI for Science Laboratory website template.

1. Rebuild Hugo output

```bash
cd /Users/Daily/Development/HP/lab-website/site
hugo --destination ../public
```

2. Verify generated files

```bash
ls -la /Users/Daily/Development/HP/lab-website/public
```

Confirm `/Users/Daily/Development/HP/lab-website/public/index.html` exists.

3. Verify Docker Compose configuration

```bash
cat /Users/Daily/Development/HP/lab-website/docker/docker-compose.yml
```

Confirm both mounts are read-only (`:ro`):
- `../public:/usr/share/nginx/html:ro`
- `../nginx/nginx.conf:/etc/nginx/nginx.conf:ro`

4. Verify Nginx configuration

```bash
cat /Users/Daily/Development/HP/lab-website/nginx/nginx.conf
```

Confirm:
- `try_files $uri $uri/ =404;`
- Security headers are present
- `server_tokens off;`

5. Start container

```bash
cd /Users/Daily/Development/HP/lab-website/docker
docker compose up -d
```

6. Confirm running status

```bash
docker compose ps
```

Confirm `lab_web` status is `Up`.

7. Check HTTP response

```bash
curl -I http://localhost
```

Confirm response includes `HTTP/1.1 200 OK`.

8. Browser validation

Open [http://localhost](http://localhost) and confirm navigation items are visible:
- Home
- Research
- Publications
- Members
- Projects
- News
- Join Us
- Contact

9. Content update smoke test

- Edit `/Users/Daily/Development/HP/lab-website/site/content/news/2026-paper.md`
- Re-run Hugo build
- Reload browser and confirm the update appears
