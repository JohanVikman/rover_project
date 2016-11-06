"""We want to control some engines using a sixaxis PS3 controller

   Remember to pair with the sixaxis controller using sixpair, do this
   while the controller is connected using USB.

   pi@raspberrypi:~/mystuff $ sudo ./sixpair
   Current Bluetooth master: 00:0d:b5:21:2e:79
   Setting master bd_addr to 00:0d:b5:21:2e:79

   You can then disconnect the controller over USB and use the
   bluetooth interface instead (press PS-button).

"""

from pygame import joystick, event, display
import RPi.GPIO as GPIO
from time import sleep
import pygame
import os
GPIO.setmode(GPIO.BOARD)

# GPIO Pin motor mapping
# A/B are directions and E is for Enabling the motor.
# Motor1 is forward/backwards
Motor1A = 16
Motor1B = 18
Motor1E = 22
# Motor1 is right/left
Motor2A = 31
Motor2B = 29                                                                   
#Motor2A = 23
#Motor2B = 21
Motor2E = 19

# PS 3 Button mapping:
UP=4
LEFT=7
RIGHT=5
DOWN=6
TRI=12
SQU=15
CIR=0
CRO=14
SEL=0
STA=3
PS3=16
LJO=1
RJO=2
L2=8
L1=10
R2=9
R1=11

def handle_button(event):
    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == UP:
            print "Going forwards"
            GPIO.output(Motor1A,GPIO.HIGH)
            GPIO.output(Motor1B,GPIO.LOW)
            GPIO.output(Motor1E,GPIO.HIGH)
        elif event.button == DOWN:
            print "Going backwards"
            GPIO.output(Motor1A,GPIO.LOW)
            GPIO.output(Motor1B,GPIO.HIGH)
            GPIO.output(Motor1E,GPIO.HIGH)
        elif event.button == RIGHT:
            print "Going right"
            GPIO.output(Motor2A,GPIO.HIGH)
            GPIO.output(Motor2B,GPIO.LOW)
            GPIO.output(Motor2E,GPIO.HIGH)
        elif event.button == LEFT:
            print "Going left"
            GPIO.output(Motor2A,GPIO.LOW)
            GPIO.output(Motor2B,GPIO.HIGH)
            GPIO.output(Motor2E,GPIO.HIGH)
    elif event.type == pygame.JOYBUTTONUP:
        print "Now stop"
        if event.button == UP or event.button == DOWN:
            GPIO.output(Motor1E,GPIO.LOW)
        if event.button == RIGHT or event.button == LEFT:
            GPIO.output(Motor2E,GPIO.LOW)
        

## Motor1 = Forwards/Backwards
## Motor2 = Right/Left
def setup_motor():
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)

    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)



setup_motor()

# USE Dummy display or else we cannot use pygame.event

os.environ["SDL_VIDEODRIVER"]="dummy"
if 1:
    #some platforms might need to init the display for some parts of pygame.
    screen = pygame.display.set_mode((1,1))


pygame.init()

#Assuming there's only on joystick connected.
stick=joystick.Joystick(0)
stick.init()

numbuttons = stick.get_numbuttons()
print("Initialized " + stick.get_name())
print("Device has {} number of buttons".format(numbuttons))

interval=0.1

try:
    done=False
    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                handle_button(event)
            if event.type == pygame.JOYBUTTONUP:
                handle_button(event)

except (KeyboardInterrupt, SystemExit):
    print("Caught kbd interrupt or systemexit")

pygame.quit()
GPIO.cleanup()
print("All done, exiting")
