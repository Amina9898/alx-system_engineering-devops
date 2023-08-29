#comment here
class nginx_redirect {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    content => "Hello, World!\n",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    content => "server {
      listen 80;
      server_name _;
      root /var/www/html;

      location / {
        return 301 http://www.example.com/redirected-page;
      }
    }",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }
}
