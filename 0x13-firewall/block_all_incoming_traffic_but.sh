#!/usr/bin/env bash
# Configures the uncomplicated firewall to accept incoming traffic on
#+ 22, 443, 80 TCP ports only

sudo apt-get update > /dev/null 2>&1
sudo apt install -y ufw > /dev/null 2>&1
echo y | sudo ufw reset
sudo systemctl stop ufw
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
echo y | sudo ufw enable
sudo systemctl enable ufw
sudo systemctl start ufw
