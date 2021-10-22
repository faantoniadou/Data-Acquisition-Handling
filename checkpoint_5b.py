# Import
from DAH import DS18B20
import time
    
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

t_start = time.time()

# The function to call each time the plot is updated

def updatePlot( i ):
    
    if i < 49:
        timeValues.append( datetime.datetime.now() ) # Store time
        measurements.append( tmp0.getCelsius() ) # Store temperature
        plotFigure.clear() # Clear the old plot
        pylab.plot( timeValues, measurements ) # Make the new plot
        pylab.xlabel("Time")
        pylab.ylabel("Temperature")
        pylab.title("Temperature of sensor against time")
    
# Make the animated plot
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=1000 )

pylab.show()

