#Create a manifest that kills a proceed named killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}