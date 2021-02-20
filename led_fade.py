#!/usr/bin/env python
#
#  auth: rbw
#  date: 20180107
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from gpiozero import LED,PWMLED
from signal import pause
from time import sleep
import logging,coloredlogs,sys,pprint,traceback 
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(sys.argv[0])
coloredlogs.install(level='DEBUG', logger=log)
pp = pprint.PrettyPrinter(indent=4)

# simple on/off code: {{{
#led = LED(14)
#for x in range(1,3):
#    print "On"
#    led.on()
#    sleep(1)
#    print "Off"
#    led.off()
#    sleep(1)
#
#exit(99)#}}}

increments = 0.2 #ie 20% (100/5=20%)
pause_len=0.1

def brighten(led):
    val = 0
    while val <= 1:
	log.debug("Brighten: [%.2f] " %val)
	led.value = val 
	sleep (pause_len)
	val += increments

def dim(led):
    val = 1
    while val >= 0:
	log.debug("Fade... : [%.2f] " %val)
	led.value = val 
	sleep (pause_len)
	val -= increments


def main():
    try:  
        led = PWMLED(14)
        log.info("Reading from GPIO pin: %s" % (led.pin))
        while True:
            brighten(led)
            dim(led)
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
