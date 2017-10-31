# Control a two motor RC car using Raspberry pi zero
This is a python3 project

## install sixaxis
Use the setup.sh script

## install python dependencies

sudo apt-get build-dep python3-pygame

python3 -m pip install wheel
python3 -m pip install pygame
python3 -m pip install rpio

## Run
Because of how we are using pygame, we need to run as root.

`sudo python3 rover_controller.py`

This should produce something like:

```xcb_connection_has_error() returned true
Initialized Sony PLAYSTATION(R)3 Controller
Device has 19 number of buttons
```