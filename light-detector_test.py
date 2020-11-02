#!/usr/bin/env python 
#
#  auth: rbw
#  date: 20180107
#  desc: 
#   https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os      
from gpiozero import LED
import pygame 

DEBUG = 1
GPIO.setmode(GPIO.BCM)

print ("Initialising sound....")
pygame.init() 
pygame.mixer.init() 
burp = pygame.mixer.Sound("../jellybaby/burp.wav")
print ("Ready....")

def RCtime (RCpin): #{{{
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.01)

    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
    return reading
#}}}

led = LED(15)
led.on()
while True:                                     
    light_resist = RCtime(27)     # Read RC timing using pin #15
    print light_resist
    if light_resist > 0: 
        print("Burp !!! ")
        led.off()
        burp.play()
        time.sleep(2)
        burp.stop()
        led.on()



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
