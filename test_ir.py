#!/usr/bin/env python
#
#  auth: rbw
#  date: 20260427
#  desc: 
#       Code started using Google AI search (gemini)
#       needs:  
#   sudo apt-get install pigpio python3-evdev
#   sudo pigpiod
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pigpio
import time

# Pin 18 is a common default for IR RX on Pi
IR_RX_PIN = 18

pi = pigpio.pi()

if not pi.connected:
    print("Could not connect to pigpio. Did you run 'sudo pigpiod'?")
    exit()

# This function runs every time the IR sensor detects a light pulse
def rx_callback(gpio, level, tick):
    print(f"Signal Change -> Level: {level} at {tick} microseconds")

# Monitor the pin for any edge (change from High to Low or vice versa)
cb = pi.callback(IR_RX_PIN, pigpio.EITHER_EDGE, rx_callback)

print(f"--- Listening on GPIO {IR_RX_PIN} ---")
print("Aim your remote at the M5 sensor and press a button.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping...")
    cb.cancel()
    pi.stop()


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
