# AI for Science Laboratory Website Template

Minimal, maintainable static laboratory website built with Hugo + Nginx + Docker.

## Structure

- `docker/docker-compose.yml`: Runtime container definition
- `nginx/nginx.conf`: Nginx static hosting configuration
- `site/`: Hugo source (theme, layouts, content, static assets)
- `public/`: Hugo build output

## Local build

```bash
cd site
hugo --destination ../public
```

## Deployment

```bash
cd docker
docker compose up -d
```

Then open `http://localhost`.

## Content update workflow

1. Edit Markdown files under `site/content/`
2. Add images under `site/static/images/`
3. Rebuild Hugo output
4. Nginx serves updated `public/`

## Security notes

- Static-only architecture (no DB, no app backend)
- Read-only volume mounts for site content and Nginx config
- Nginx security headers enabled
- `server_tokens off` to reduce fingerprinting

## Future extension ideas

- BibTeX-based publication generation
- Google Scholar synchronization
- RSS feed for news
- Alumni archive automation
- Visualization section for research assets
# hp
