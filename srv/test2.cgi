#!/usr/bin/ruby

puts "Content-Type: text/plain;charset=utf-8\n\n"

remote = ENV['REMOTE_ADDR'] || 'EMPTY'
puts "Connexion depuis: #{remote}"
if remote == '::1' or remote == '127.0.0.1'
  puts "OK: la connexion est bien etablie depuis une adresse locale"
else
  puts "ERREUR: la connexion n'est pas établie depuis une adresse locale. Les données ont circulé en clair sur le réseau."
end
