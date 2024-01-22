#!/usr/bin/env bash
# Setup a Web server for deployment of web_static
apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" > /data/web_static/releases/test/index.html

rm -rf /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

conf="/etc/nginx/sites-available/default"
sed -i '/^# alias for hbnb_static$/s/^#//' "$conf"
if ! grep -q "location /hbnb_static {" "$conf"; then
	sed -i '/^server {/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$conf"
fi
service nginx restart
