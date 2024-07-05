# Install and configure nginx server

exec { 'nginx-repo':
  command => 'sudo add-apt-repository ppa:nginx/stable',
  path    => '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin',
}

exec { 'update-index':
  command => 'apt-get update',
  path    => '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['nginx-repo', 'update index'],
}

exec { 'HTTP-allow':
  command => "ufw allow 'Nginx HTTP'",
  path    => '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin',
  onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
}

exec { '/var/www-permissions':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin',
}

file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page \n"
}

file { 'default-config':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
		root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
		try_files \$uri \$uri/ =404;
	}

	error_page 404 /404.html;
	location /404.html {
		internal;
	}

	if (\$request_filename ~ redirect_me) {
		rewrite ^ https://www.google.com permanent;
	}
}
",
}

exec { 'restart-nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
