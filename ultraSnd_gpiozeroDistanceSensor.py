#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210718
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import DistanceSensor
import time

ultrasonic = DistanceSensor(echo=15, trigger=14)

while True:
    print(ultrasonic.distance)
    time.sleep(.250)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
