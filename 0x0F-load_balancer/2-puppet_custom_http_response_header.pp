# Appends a custom HTTP response header
exec { 'Nginx':
  command  => 'sudo apt-get -y update;
  sudo apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-availale/default;
  sudo service nginx restart',
  provider => shell,
}
