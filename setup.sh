#!/bin/bash

pip install dbus
echo "Installing deps"
apt-get install bluez bluez-hcidump checkinstall libusb-dev libbluetooth-dev joystick pyqt4-dev-tools

echo "Getting sixaxis pairing util"
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb

echo "Getting sixad tool"
wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
tar xfvz QtSixA-1.5.1-src.tar.gz
cd QtSixA-1.5.1/sixad
rm shared.h
wget https://bugs.launchpad.net/qtsixa/+bug/1036744/+attachment/3260906/+files/compilation_sid.patch
patch ~/QtSixA-1.5.1/sixad/shared.h < compilation_sid.patch

make
sudo mkdir -p /var/lib/sixad/profiles
sudo checkinstall

sudo ./sixpair
sudo sixad --start


