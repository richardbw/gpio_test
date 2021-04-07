#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210407
#  desc: 
#   https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import MotionSensor, LED, Buzzer
from signal import pause

print('''
PIR pins: 5V, GND, GPIO14
LED     :     GND, GPIO15
Buzzer  :     GND, GPIO27
''')

pir = MotionSensor(14)
led = LED(15)
buzzer = Buzzer(27)

def when_motion():
    print("Motion detected")
    led.on()
    buzzer.beep()


def when_no_motion():
    print("Motion stopped")
    led.off()
    buzzer.off()

pir.when_motion = when_motion
pir.when_no_motion = when_no_motion

print("Running...")
pause()


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("Done.")
#//EOF
