# Install and configure nginx server

exec { 'update index':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update index'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

exec { 'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.google.com permanent;" /etc/nginx/sites-available/default'
  provider => 'shell',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
