#!/usr/bin/env bash
# Bash script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo echo "
server {
        listen 80 default_server;
        location /hbnb_static { alias /data/web_static/current/;}
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        add_header X-Served-By \$hostname;
        location /redirect_me {
        return 301 http://google.com/;
        }
        error_page 404 /404.html;
        location = /404.html {
                internal;
        }
}" | tee /etc/nginx/sites-enabled/default
sudo service nginx restart
