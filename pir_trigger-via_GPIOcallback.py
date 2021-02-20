#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210217
#  desc: 
#   from: https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import RPi.GPIO as GPIO
import time
 
SENSOR_PIN = 14
print("""
GPIOcallback:
OUT is centre - to GPIO14
""")

 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(SENSOR_PIN, GPIO.IN)
 
def my_callback(channel):
    # Here, alternatively, an application / command etc. can be started.
    print('There was a movement!')
 
try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
    print('Starting...!')
    while True:
        print('.', end='',sep='',flush=True)
        time.sleep(.5)
except KeyboardInterrupt:
    print("Finish...")
GPIO.cleanup()


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print( "Done." )
#//EOF
