# Import I/O expander chip library
from DAH import PCF8574
import time

# Setup chip
pcf = PCF8574(address=0x38)

# A variable to store the pin number for the LED
LED0 = 0
SWITCH0 = 7

# Turn off the LED by setting the pin high
pcf.digitalWrite(LED0, True)

# Loop for ever
while True:
    # Christmas Lights pattern
    time.sleep(0.5)
    pcf.portWrite(10)
    time.sleep(0.5)
    pcf.portWrite(5)
    
    # Read the switch - if it is pressed change the LED outputs
    if ( pcf.digitalRead(SWITCH0)==False ):
        # 2 consecutive lights turning on pattern
        time.sleep(0.5)
        pcf.portWrite(3)
        time.sleep(0.5)
        pcf.portWrite(12)
