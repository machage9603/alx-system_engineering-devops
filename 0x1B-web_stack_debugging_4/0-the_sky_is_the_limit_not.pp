# Puppet manifest to fix web server setup to handle high pressure

# Fix for Nginx configuration
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/worker_connections  768;/worker_connections  4096;/" /etc/nginx/nginx.conf',
}

# Restart Nginx service after configuration change
service { 'nginx':
  ensure => running,
  enable => true,
  require => Exec['fix--for-nginx'],
}
