#!/bin/bash
#Install Anonsurf
git clone https://github.com/Und3rf10w/kali-anonsurf.git
chmod 777 -R kali-anonsurf
cd kali-anonsurf
./installer.sh
sudo anonsurf start

#Install tor Browser
sudo apt install tor torbrowser-launcher
sudo torbrowser-launcher
