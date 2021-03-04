# gpio_test

Also [gpiozero basic recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html)

Basic LED convention:
* GPIO14 (8th pin)
* GND (eg 9th pin)

_Check that the connection is the right way around!_


Simple LED setup:<br/>
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210220_171910.jpg" width="550"/>


<br/>
Simple LED setup, with resistor:<br/>
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210220_171927.jpg" width="550"/>

<br/>
Simple PIR setup:<br/>
**Note**: 

- VCC is on left/red, to 5V
- GND is on rght/grey, to '-'
- OUT is centre/brown, to GPIO14 (not like picture, which is ..15)
<br/>
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210220_155255.jpg" width="550"/>

<br/>
LightSensor/Light Dependent Resistor(LDR) setup:<br/>
- Power (red here) is 3V
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210303_115641.jpg" width="550"/>

<br/>
LDR, with LED that dims in bright light (straigt from [gpiozero basic recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html)):<br/>
<img src="https://raw.githubusercontent.com/richardbw/gpio_test/main/img/20210304_101653.jpg" width="550"/> 
