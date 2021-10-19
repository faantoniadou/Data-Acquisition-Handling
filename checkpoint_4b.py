# Import I/O expander chip library
from DAH import PCF8574
import time

# Setup chip
pcf = PCF8574(address=0x38)

# A variable to store the pin number for the LED
LED0 = 0
LED1 = 1
LED2 = 2
LED3 = 3

# Turn off the LED by setting the pin high
pcf.digitalWrite(LED0, True)
pcf.digitalWrite(LED1, True)
pcf.digitalWrite(LED2, True)
pcf.digitalWrite(LED3, True)

# Christmas Lights
count = 0
while count < 4:
    count += 1
    time.sleep(0.5)
    pcf.portWrite(10)
    time.sleep(0.5)
    pcf.portWrite(5)


pcf.digitalWrite(LED0, True)
pcf.digitalWrite(LED1, True)
pcf.digitalWrite(LED2, True)
pcf.digitalWrite(LED3, True)

# To explain how portWrite works we define 1 as the state where the LED is off and 0 when the LED is on.
# Looking at the LEDs from the bottom up we note the outcome of each of the following:

# pcf.portWrite(0)  #0000
# pcf.portWrite(1)  #0001
# pcf.portWrite(2)  #0010
# pcf.portWrite(3)  #0011
# pcf.portWrite(4)  #0100
# pcf.portWrite(5)  #0101
# pcf.portWrite(6)  #0110
# pcf.portWrite(7)  #0111
# pcf.portWrite(8)  #1000
# pcf.portWrite(9)  #1001
# pcf.portWrite(10) #1010
# pcf.portWrite(11) #1011
# pcf.portWrite(12) #1100

# each outcome corresponds to the binary representation of the digit given as the input of the portWrite method.
# so the output of the method is the binary representation of the input as shown by the LEDs.






