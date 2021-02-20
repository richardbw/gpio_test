#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210218
#  desc: 
#   https://projects.raspberrypi.org/en/projects/parent-detector/3
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import time
from gpiozero import MotionSensor
pir = MotionSensor(15)


while True:
    print('.', end='',sep='',flush=True)
    time.sleep(1)
    pir.wait_for_motion()
    print("Motion detected!")



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print( "Done." )
#//EOF
