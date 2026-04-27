#!/usr/bin/env python
#
#  auth: rbw
#  date: 20260427
#  desc: 
#      Code started using Google AI search (gemini)
#      Needs:
#   sudo apt-get install python3-evdev
#   
#      GPIO pin no.s set in /boot/config.txt
#
#      For debugging, needed:
#   sudo apt-get install lirc -y
#   sudo mode2 -d /dev/lirc1                   #show raw input 
#   sudo apt-get install ir-keytable
#   sudo ir-keytable --sysdev rc1 -p all -t    #show scan codes
#
#   NEEDED THIS TO START WORKING!    
#   sudo systemctl stop lircd
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import evdev
from evdev import InputDevice, categorize, ecodes

def find_ir_device(): # Look for the device named 'gpio_ir_recv'
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "gpio_ir_recv" in device.name:
            return device
    return None

device = find_ir_device()

if device:
    print(f"""
Run this 1st: sudo ir-keytable --sysdev rc1 -p all

Connected to: {device.name} at {device.path}
Press remote buttons see their codes...""")

    button_map = { #{{{
         0x408: "POWER",
         0x411: "CH_01",
         0x412: "CH_02",
         0x413: "CH_03",
         0x414: "CH_04",
         0x415: "CH_05",
         0x416: "CH_06",
         0x417: "CH_07",
         0x418: "CH_08",
         0x419: "CH_09",
         0x402: "VOL_UP",
         0x403: "VOL_DN",
         0x409: "MUTE",
         0x400: "PRG_UP",
         0x401: "PRG_DN",
         0x440: "ARR_UP",
         0x441: "ARR_DN",
         0x407: "ARR_LFT",
         0x406: "ARR_RGT",
         0x47c: "HOME",
         0x444: "OK",
         0x472: "RED",
         0x471: "GREEN",
         0x463: "YELLOW",
         0x461: "BLUE",
    } #}}}

    try:
        for event in device.read_loop():
            #print(f"{dir(event)}: {event}")
            if event.type == ecodes.EV_MSC and event.code == ecodes.MSC_SCAN:
                scancode = event.value
                button_name = button_map.get(scancode, "Unknown Button")
                print(f"Scancode: {hex(scancode)} | Button: {button_name}")
    except KeyboardInterrupt:
        print("\nExiting...")
else:
    print("IR Receiver not found. Check your /boot/config.txt and wiring.")


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
