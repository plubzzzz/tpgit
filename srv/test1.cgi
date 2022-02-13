#!/usr/bin/ruby

require 'resolv'

puts "Content-Type: text/plain;charset=utf-8\n\n"

remote = ENV['REMOTE_ADDR'] || 'EMPTY'
puts "Connexion depuis: #{remote}"
cli = IPSocket.getaddress("cli.local")
puts "Adresse de cli.local: #{cli}"
if remote != cli
  puts "Erreur: la connexion n'est pas établie depuis l'adresse de la VM cli (#{cli}), mais depuis #{remote}"
else
  puts "OK: la connexion est bien établie depuis l'adresse de la VM cli"
end
