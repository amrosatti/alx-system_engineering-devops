# Executes a command that kills a process

exec { 'kill':
  command => 'pkill -9 killmenow',
  path    => '/usr/bin',
}
