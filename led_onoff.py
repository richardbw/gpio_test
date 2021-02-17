#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20180107
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import LED

import logging,coloredlogs,sys,pprint,traceback 
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(sys.argv[0])
coloredlogs.install(level='DEBUG', logger=log)
pp = pprint.PrettyPrinter(indent=4)


led_state = True
led_pin = 15


log.info("LED GPIO pin: %s"%led_pin)
log.info("put other pin in GRD (and get them the right way around!)")


def main():
    global led_state, led_pin
    try:  
        led = LED(led_pin)
        led.on()
        while True:
            txt = input("Type [Enter]: ")
            led_state = not led_state
            if led_state:
                led.on()
            else:
                led.off()
            log.info("LED state: %s" % led_state)

    except KeyboardInterrupt:  
        log.info("...^C pressed...")
    except:  
        log.error(str(sys.exc_info()[1]))
        log.error(traceback.format_tb(sys.exc_info()[2]))
    finally:  
        log.info("Cleaning up/closing.")
        led.close() # this ensures a clean exit 

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__": main()
log.info("Done.")
#//EOF
