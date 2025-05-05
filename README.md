<img src="https://img.shields.io/badge/Livin-the%20crazy%20life-brightgreen?logo=github"/>

# gpio_test

Also [gpiozero basic recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html)

Basic LED convention:
* GPIO14 (8th pin)
* GND (eg 9th pin)

_Check that the connection is the right way around!_

  * [Simple LED setup](#simple-led-setup)
  * [Simple LED setup, with resistor:](#simple-led-setup--with-resistor-)
  * [Simple PIR setup](#simple-pir-setup)
  * [LightSensor/Light Dependent Resistor(LDR) setup](#lightsensor-light-dependent-resistor-ldr--setup)
  * [LDR, with LED that dims in bright light](#ldr--with-led-that-dims-in-bright-light)
  * [Ultrasound Distance detection](#ultrasound-distance-detection)
    + [With Buzzer](#with-buzzer)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>




## Simple LED setup
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210220_171910.jpg" width="550"/>

## Simple LED setup, with resistor:
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210220_171927.jpg" width="550"/>


## Simple PIR setup
**Note**: 
- VCC is on left/red, to 5V
- GND is on rght/grey, to '-'
- OUT is centre/brown, to GPIO14 (not like picture, which is ..15)

<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210220_155255.jpg" width="550"/>

## LightSensor/Light Dependent Resistor(LDR) setup
- Power (red here) is 3V



<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210303_115641.jpg" width="550"/>

##  LDR, with LED that dims in bright light
(straight from [basic recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html))

<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210304_101653.jpg" width="550"/> 



## Ultrasound Distance detection
Taken from [physical-computing](https://projects.raspberrypi.org/en/projects/physical-computing/12), and layout hints from [pi tutorials](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)
- VCC, Red, 5V/ phys.2
- GND, Brown, phys.6
- Trigger, Orange, GPIO14 (8)
- Echo, Yellow, GPIO15 (10)

<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210718_125040.jpg" width="550"/> 

### With Buzzer
Same as above, with:
- GPIO4 (7)
- GND (9)

<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210718_180056.jpg" width="250"/> <br/>
Micro:bit version (1κΩ resistor in Echo line; idea taken from [here](https://firialabs.com/blogs/lab-notes/ultrasonic-distance-sensor-with-python-and-the-micro-bit))
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20250505_121631.jpg" width="250"/> 



