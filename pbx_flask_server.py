#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20201101
#  desc: 
#           https://stoplight.io/blog/python-rest-api/
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from    gpiozero    import LED
from    flask       import Flask, json, Response, jsonify
import  logging,coloredlogs,sys,pprint,traceback 

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(sys.argv[0])
coloredlogs.install(level='DEBUG', logger=log)
pp = pprint.PrettyPrinter(indent=4)

api = Flask(__name__)

led_state = {"state": False, "pin": 15}
led = LED(led_state["pin"])



@api.route('/flip_led', methods=['GET'])
def flip_led():
    led_state['state'] = not led_state['state'] 

    if led_state['state']:
        led.on()
    else:
        led.off()

    return json.dumps(led_state), 201,  {'Content-Type': 'application/json'}



@api.route('/companies', methods=['POST'])
def post_companies():
  return json.dumps({"success": True}), 201



if __name__ == '__main__':
    log.info("Plug LED leads into no.15 & GRND (eg 9)")
    api.run(host='0.0.0.0')





#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("Done.")
#//EOF
