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
#while count < 4:
#    count += 1
#    time.sleep(0.5)
#    pcf.portWrite(10)
#    time.sleep(0.5)
#    pcf.portWrite(5)
#time.sleep(0.5)

#pcf.portWrite(0) #1111
#time.sleep(0.5)
#pcf.portWrite(1) #0111
# time.sleep(0.5)
#pcf.portWrite(2)
# time.sleep(0.5) #1011
#pcf.portWrite(3) #0011
# time.sleep(0.5)
#pcf.portWrite(4) #1101
# time.sleep(0.5)
#pcf.portWrite(5)  #0101
#time.sleep(0.5)
#pcf.portWrite(6) #1001
#time.sleep(0.5)
#pcf.portWrite(7) #0001
#time.sleep(0.5)
#pcf.portWrite(8) #1110
#pcf.portWrite(9) #0110
#pcf.portWrite(10) #1010
#pcf.portWrite(11) #0010
#pcf.portWrite(12) #1100
time.sleep(0.5)
#pcf.portWrite(4)



pcf.digitalWrite(LED0, True)
pcf.digitalWrite(LED1, True)
pcf.digitalWrite(LED2, True)
pcf.digitalWrite(LED3, True)



