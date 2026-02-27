#! /bin/bash

git clone https://github.com/tomaspinho/rtl8821ce
chmod 777 -R rtl8821ce
cd rtl8821ce
sudo apt-get install bc module-assistant build-essential dkms
sudo m-a prepare
sudo ./dkms-install.sh
sudo reboot

#lspci | grep Network