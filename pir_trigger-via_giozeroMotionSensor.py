#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210218
#  desc: 
#   https://projects.raspberrypi.org/en/projects/parent-detector/3
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import MotionSensor
import time

pir = MotionSensor(14)
print("""
gpiozero wait_for_motion:
OUT is centre - to GPIO14
""")

while True:
    pir.wait_for_motion()
    print("Motion detected!")
    time.sleep(.500)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print( "Done." )
#//EOF
