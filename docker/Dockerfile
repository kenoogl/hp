FROM nginx:stable

# Use repository nginx config for production container.
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Serve prebuilt Hugo output without host bind mounts.
COPY public/ /usr/share/nginx/html/
