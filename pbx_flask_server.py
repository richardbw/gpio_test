#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20201101
#  desc: 
#           https://stoplight.io/blog/python-rest-api/
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from    gpiozero    import LED
from    flask       import Flask, json, Response, jsonify
import  logging,coloredlogs,sys,pprint,socket

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(sys.argv[0])
coloredlogs.install(level='DEBUG', logger=log)
pp = pprint.PrettyPrinter(indent=4)

api = Flask(__name__)

port=1234
led_state = {"state": False, "pin": 14}
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
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # get IP address, to show URL https://stackoverflow.com/a/166589
    log.info("port:API path: http://%s:%s/flip_led" % (s.getsockname()[0], port))
    s.close()

    log.info("Plug LED leads into no.14 & GRND (eg 8)")
    api.run(host='0.0.0.0', port=port)





#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("Done.")
#//EOF
