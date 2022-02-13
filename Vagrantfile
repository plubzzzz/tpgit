Vagrant.configure("2") do |config|
  config.vm.provider "libvirt" do |vb|
    vb.memory = "1024"
    vb.cpus = 1
  end

  # On all machines, see https://www.vagrantup.com/docs/provisioning/basic_usage.html
  config.vm.provision "shell", inline: <<-SHELL
    set -ex
    apt-get update
    apt-get -y install libnss-mdns
    useradd --shell /bin/bash --create-home alice || true
    useradd --shell /bin/bash --create-home bob || true
    useradd --shell /bin/bash --create-home carol || true
    echo patrick:azerty123 | chpasswd
    echo alice:1234 | chpasswd
    echo bob:azerty | chpasswd
    echo carol:secret | chpasswd
    echo Enabling password auth
    sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
    systemctl restart ssh.service
  SHELL

  config.vm.define "cli" do |b|
    b.vm.box = "debian/stretch64"
    b.vm.network "private_network", ip: "192.168.57.2"
    b.vm.hostname = "cli"
  end

  config.vm.define "srv" do |b|
    b.vm.box = "debian/stretch64"
    b.vm.network "private_network", ip: "192.168.57.3"
    b.vm.hostname = "srv"

    b.vm.provision "shell", inline: <<-SHELL
      apt-get -y install apache2 ruby php
      a2enmod cgi php
      systemctl restart apache2.service
      cp /vagrant/srv/test1.cgi /usr/lib/cgi-bin/test1.cgi
      cp /vagrant/srv/test2.cgi /usr/lib/cgi-bin/test2.cgi
    SHELL
  end

end
# vim: ft=ruby syn=ruby fileencoding=utf-8 sw=2 ts=2 ai eol et si
