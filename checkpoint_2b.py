# Import DAC chip library
from DAH import MCP4922
import time

# Define DAC as SPI chip 1 (CE1/GPIO7)
DAC1 = MCP4922( chip=1 )

# Set a series of different values for the output voltage of the DAC
output_volt = [0,0.5,1.0,1.5,2.0,2.5,3.0,0.0]

for i in range(len(output_volt)):                   # loop to change output of the DAC
    DAC1.analogWriteVolt( 0, output_volt[i] )

    time.sleep(1.0)                                 # leave time between changes

