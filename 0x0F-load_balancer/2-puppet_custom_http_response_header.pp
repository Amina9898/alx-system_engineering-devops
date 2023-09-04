# 2-puppet_custom_http_response_header.pp

# Define a custom fact to get the server's hostname
Facter.add('custom_hostname') do
  setcode 'hostname'
end

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create a custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => 'present',
  content => "
server {
    listen 80 default_server;
    server_name _;

    location / {
        add_header X-Served-By $::custom_hostname;
        # Your other location settings here
    }
}
",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => File['/etc/nginx/conf.d/custom_headers.conf'],
}

