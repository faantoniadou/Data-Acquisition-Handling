# Import
from DAH import DS18B20
import time
# Readout temperature sensor
for i in range(10):
    
    
    print(tmp0.getCelsius())
    time.sleep(1)
    i += 1
    
#print(tmp0.getCelsius())
    
import pylab
import matplotlib.animation as animation
import datetime
# Empty arrays of time and measurement values to plot
timeValues = [ ]
measurements = [ ]
# Set up the plot object
plotFigure = pylab.figure()
tmp0 = DS18B20( address="10-000803472a99" )

# The function to call each time the plot is updated
def updatePlot( i ):
    timeValues.append( datetime.datetime.now() ) # Store time
    measurements.append( tmp0.getCelsius() ) # Store temperature
    plotFigure.clear() # Clear the old plot
    pylab.plot( timeValues, measurements ) # Make the new plot
    
# Make the animated plot
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=1000 )
pylab.show()
