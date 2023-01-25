# task 0 using ppupet

package { 'nginx':
  ensure => 'present',
}

file { ['/data',
        '/data/web_static',
        '/data/web_static/releases',
        '/data/web_static/shared',
        '/data/web_static/releases/test',]:
  ensure => 'directory',
  before => File['/data/web_static/releases/test/index.html']
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Hello Holberton',
}

exec { 'test -L':
  path    => 'usr/bin/env bash',
  command => 'test -L /data/web_static/current && sudo rm /data/web_static/current',
  require => File['/data/web_static/releases/test/index.html'],
}

exec { 'ln -s':
  path    => 'usr/bin/env bash',
  command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
  require => Exec['test -L'],
}

exec { 'chown':
  path    => 'usr/bin/env bash',
  command => 'sudo chown -R ubuntu:ubuntu /data',
  require => Exec['ln -s'],
}

exec { 'sed -i':
  path    => 'usr/bin/env bash',
  command => 'sudo sed -i "36i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t} /etc/nginx/sites-enabled/default',
  require => Package['nginx'],
  notify  => Exec['nginx'],
}

exec { 'nginx':
  path    => 'usr/bin/env bash',
  command => 'sudo service nginx restart',
  require => Exec['sed -i'],
}
