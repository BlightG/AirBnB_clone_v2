# task 0 using ppupet

package { 'nginx':
  ensure => 'present',
}

exec { 'mkdir -p':
  path    => ['/usr/bin','/usr/sbin/','/bin'],
  command => 'sudo mkdir -p /data/web_static/shared/ ;sudo  mkdir -p /data/web_static/releases/test/',
  before  => Exec['touch'],
}

exec { 'touch':
  path    => '/usr/bin/',
  command => 'touch /data/web_static/releases/test/index.html',
  before  => File['/data/web_static/releases/test/index.html'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Hello Holberton',
}

exec { 'test -L':
  path    => '/usr/bin/',
  command => 'test -L /data/web_static/current &&  rm /data/web_static/current',
  require => File['/data/web_static/releases/test/index.html'],
}

exec { 'ln -s':
  path    => '/usr/bin/',
  command => 'ln -s /data/web_static/releases/test/ /data/web_static/current',
  require => Exec['test -L'],
}

exec { 'chown':
  path    => '/usr/bin/',
  command => 'chown -R ubuntu:ubuntu /data',
  require => Exec['ln -s'],
}

exec { 'sed -i':
  path    => '/usr/bin/',
  command => 'sed -i "36i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t} /etc/nginx/sites-enabled/default',
  require => Package['nginx'],
  notify  => Exec['nginx'],
}

exec { 'nginx':
  path    => '/usr/bin/',
  command => 'service nginx restart',
  require => Exec['sed -i'],
}
