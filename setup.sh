apt-get update
apt-get install python-dev python-pip git libmysqlclient-dev nginx
pip install -r requirements.txt
rm -f /etc/nginx/sites-enabled/default
cp confs/nginx.conf /etc/nginx/sites-enabled/testapp
service nginx reload
