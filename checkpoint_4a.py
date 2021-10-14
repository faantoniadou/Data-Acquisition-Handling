# Import I/O expander chip library
from DAH import PCF8574
import time

# Setup chip
pcf = PCF8574(address=0x38)

# A variable to store the pin number for the LED
LED0 = 0

# Turn off the LED by setting the pin high
pcf.digitalWrite(LED0, True)

# Insert your code here
count = 0
while count < 10:
    count += 1
    pcf.digitalWrite(LED0, False)
    time.sleep(0.5)
    pcf.digitalWrite(LED0, True)
    time.sleep(0.5)
