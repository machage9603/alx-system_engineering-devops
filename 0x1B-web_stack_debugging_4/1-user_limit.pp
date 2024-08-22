# Ensure the soft and hard nofile limits are set correctly
file_line { 'set-soft-nofile-limit':
  path  => '/etc/security/limits.conf',
  line  => '* soft nofile 8192',
  match => '^* soft nofile',
}

file_line { 'set-hard-nofile-limit':
  path  => '/etc/security/limits.conf',
  line  => '* hard nofile 8192',
  match => '^* hard nofile',
}

# Notify user about successful configuration change
notify { 'User limit issue fixed':
  message => 'User limit issue has been resolved successfully.',
  require => [File_line['set-soft-nofile-limit'], File_line['set-hard-nofile-limit']],
}
