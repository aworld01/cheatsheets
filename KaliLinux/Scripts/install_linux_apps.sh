#!/bin/bash

###Linux packages
apt install python3-pip -y
apt install code -y
apt install libreoffice
apt install vlc
#apt install figlet
#apt install blender

##to install pillow module for python3
apt install python3-pil python3-pil-imagetk





###Python3 packages
## Install Pyaudio
apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
apt install ffmpeg libav-tools
pip install pyaudio
apt update

##to install playsound module for python3.
pip3 install playsound

##to install Kivy for python3.
pip3 install kivy
pip3 install kivymd




###other packages
##Install Anonsurf
git clone https://github.com/Und3rf10w/kali-anonsurf.git
chmod 775 -R kali-anonsurf
cd kali-anonsurf
./installer.sh

#Install tor Browser
apt install tor torbrowser-launcher
torbrowser-launcher