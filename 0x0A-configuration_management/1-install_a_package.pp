# Installs 'flask' from 'pip3'

exec { 'flask':
  command   => 'pip3 install flask==2.1.0',
  path      => '/usr/bin',
  unliss    => 'pip3 list | grep flask',
}
