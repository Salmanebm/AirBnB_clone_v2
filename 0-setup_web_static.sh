#!/usr/bin/env bash
# Setting up my web servers

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo chmod 777 /etc/nginx/sites-available/default

sudo echo "server {
  listen 80 default_server;
  listen [::]:80 default_server;
  add_header X-Served-By $HOSTNAME;
  root   /var/www/html;
  index  index.html index.htm;

  location /hbnb_static {
    alias /data/web_static/current;
    index index.html index.htm;
  }

  location /redirect_me {
    return 301 http://cuberule.com/;
  }

  error_page 404 /404.html;
  location /404 {
    root /var/www/html;
    internal;
  }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
