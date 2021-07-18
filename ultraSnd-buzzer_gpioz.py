#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210718
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import Buzzer,DistanceSensor
from time import sleep

buzzer = Buzzer(4)
ultrasonic = DistanceSensor(echo=15, trigger=14)

while True:
    sl_t = ultrasonic.distance
    print(sl_t)
    buzzer.on()
    sleep(sl_t)
    buzzer.off()
    sleep(sl_t)



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
