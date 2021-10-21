# Import
from DAH import DS18B20
import time
    
#print(tmp0.getCelsius())
    
import pylab
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import datetime

# Empty arrays of time and measurement values to plot
timeValues = []
measurements1 = []
measurements2 = []
# Set up the plot object
plotFigure = pylab.figure()
tmp0 = DS18B20( address="10-000803472a99" )
tmp1 = DS18B20( address="10-000803472fa1" )

t_start = time.time()

# The function to call each time the plot is updated

def updatePlot( i ):
    
    if i < 19:
        timeValues.append( datetime.datetime.now() ) # Store time
        measurements1.append( tmp0.getCelsius() ) # Store temperature
        measurements2.append( tmp1.getCelsius() ) # Store temperature
        
        plotFigure.clear() # Clear the old plot
        pylab.plot( timeValues, measurements1, label='sensor 1' ) # Make the new plot
        pylab.plot( timeValues, measurements2, label='sensor 2' )
        pylab.xlabel("Time")
        pylab.ylabel("Temperature")
        pylab.title("Temperature of sensors against time")
        pylab.legend()
        #t_finish = time.time()
        #t_int = t_finish - t_start
        #count +=1
        print(i)
        #i += 1

    
# Make the animated plot
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=1000 )
pylab.show()

sensor1_vals = np.asarray(measurements1)
sensor2_vals = np.asarray(measurements2)

print('Sensor 1 mean: ' + str(np.mean(sensor1_vals)))
print('Sensor 1 standard deviation: ' + str(np.std(sensor1_vals)))

print('Sensor 2 mean: ' + str(np.mean(sensor2_vals)))
print('Sensor 2 standard deviation: ' + str(np.std(sensor2_vals)))

#print to determine resolution
print(sensor1_vals)
print(sensor2_vals)
#0.062

plt.hist(sensor1_vals, bins=5, range=[23.75,24.])#range=[np.min(np.min(sensor1_vals),np.min(sensor2_vals)),np.max(np.max(sensor1_vals),np.max(sensor2_vals))])
plt.hist(sensor2_vals, bins=5, range=[23.75,24.])#range=[np.min(np.min(sensor1_vals),np.min(sensor2_vals)),np.max(np.max(sensor1_vals),np.max(sensor2_vals))])

plt.show()