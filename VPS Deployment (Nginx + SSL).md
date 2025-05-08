## 🌐 2. VPS Deployment (Nginx + SSL)

### 🛠️ Requirements

* Ubuntu VPS
* Domain (e.g. `htb-chat.yourdomain.com`)
* Ports `80` and `443` open
* Docker & Docker Compose installed

---

### 🧱 Setup Steps

#### 1. SSH Into VPS and Clone Project

```bash
ssh user@your-vps-ip
git clone https://github.com/herisatry/htb-pdf-chatbot.git
cd htb-pdf-chatbot
```

#### 2. Start App Locally (Internal Only)

```bash
./start.sh
```

This runs the Streamlit app on `localhost:8501`.

---

#### 3. Install Nginx + Certbot

```bash
sudo apt update
sudo apt install nginx certbot python3-certbot-nginx -y
```

---

#### 4. Nginx Reverse Proxy

Create file: `/etc/nginx/sites-available/htb`

```nginx
server {
    listen 80;
    server_name htb-chat.yourdomain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable it:

```bash
sudo ln -s /etc/nginx/sites-available/htb /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

#### 5. Add HTTPS (SSL)

```bash
sudo certbot --nginx -d htb-chat.yourdomain.com
```

Now your chatbot is live on HTTPS 🎉
