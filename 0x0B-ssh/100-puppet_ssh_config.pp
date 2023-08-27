#Create stuff
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
}

file_line { 'Refuse password auth':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
}
