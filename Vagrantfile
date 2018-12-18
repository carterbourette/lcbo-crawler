# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"

    config.vm.network "private_network", ip: "172.30.1.8"
    config.vm.network "forwarded_port", guest: 80, host: 8870
    config.vm.network "forwarded_port", guest: 3306, host: 8871
    config.vm.synced_folder "./", "/var/www", create: false, group: "vagrant", owner: "vagrant"

    config.vm.define "devlocal" do |devlocal|
       devlocal.vm.hostname = 'devlocal' # Setting up hostname
       devlocal.vm.provision "shell", path: "provision.sh"
   end
end
