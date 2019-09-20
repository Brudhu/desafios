#!/bin/bash


#sudo apt-get install python3-venv
#sudo apt-get install python3-pip
if ! [ $(id -u) = 0 ]; then

   echo "The script need to be run as root." >&2

   exit 1

fi

if [ $SUDO_USER ]; then
    real_user=$SUDO_USER
else
    real_user=$(whoami)
fi

sudo -u $real_user wget https://github.com/mozilla/geckodriver/releases/download/v0.25.0/geckodriver-v0.25.0-linux64.tar.gz

sudo -u $real_user tar -xvzf geckodriver*

sudo -u $real_user chmod +x geckodriver

mv geckodriver /usr/bin/

sudo -u $real_user rm geckodriver*
