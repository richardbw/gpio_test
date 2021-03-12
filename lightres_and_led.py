#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210312
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import LightSensor, PWMLED
import time

LDR_PIN=14
LED_PIN=15
print ("Control pin for lightResistor is [%s], and +ve for LED pin is [%s]." % (LDR_PIN, LED_PIN))

sensor = LightSensor(LDR_PIN)
led = PWMLED(LED_PIN)


led.source = sensor

print ("Starting...")
try: 
    print ("Sensor value:")
    while True:
        print(sensor.value)
        time.sleep(.5)

except KeyboardInterrupt:
    print("Finish...")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
