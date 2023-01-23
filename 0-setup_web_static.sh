#!/usr/bin/env bash
# a bashscript that sets up a webserver

sudo apt update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Best School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html
test -L /data/web_static/current && sudo rm /data/web_static/current

ln -s /data/web_static/releases/test/ /data/web_static/current
new_location=" \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "36i\\$new_location" /etc/nginx/sites-enabled/default
sudo service nginx restart
