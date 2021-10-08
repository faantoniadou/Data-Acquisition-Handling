# Import DAC chip library
from DAH import MCP4922
import time
import numpy as np
    
# Import ADC chip library
from DAH import MCP3208
 
# Define DAC as SPI chip 1 (CE1/GPIO7)
DAC1 = MCP4922( chip=1 )

# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )

#create array to change output of the DAC
output_volt = np.linspace(0,3,50)

for i in range(len(output_volt)):
    
    DAC1.analogWriteVolt( 0, output_volt[i] )           # changes DAC output
    
    print( ADC0.analogReadVolt(1) )                     # prints voltage read by the ADC
    
    time.sleep(0.2)                                     # leaves increments between measurements
    
DAC1.analogWriteVolt( 0, 0 )                            # turn LED off at the end

