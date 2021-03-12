#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210217
#  desc: 
#   https://projects.raspberrypi.org/en/projects/physical-computing/8
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(14)

while True:
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print( "Done." )
#//EOF
