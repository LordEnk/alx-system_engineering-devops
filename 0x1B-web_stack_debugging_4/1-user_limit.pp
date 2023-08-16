# Enable the user holberton to login and open files without error

# modify file limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  content => "holberton hard nofile 65535\nholberton soft nofile 65535\n",
  require => User['holberton'],
}
