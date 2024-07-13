#Install flask from pip3 using Puppet

package { 'python3-pip':
  ensure  => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['usr/bin'],
  environment => ['LC_ALL=en_US.UTF-8', 'LANG=en_US.UTF-8'],
  creates     => '/usr/local/lib/python3.8/dist-packages/Flask-2.1.0.dist-info',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}