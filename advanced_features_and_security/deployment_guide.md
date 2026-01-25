# Deployment Guide for HTTPS

To support the Django security settings, the web server (Nginx/Apache) must be configured with SSL/TLS certificates.

## Nginx Configuration Example
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_set_header X-Forwarded-Proto https;
        proxy_pass http://localhost:8000;
    }
}
