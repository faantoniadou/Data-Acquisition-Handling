    
#print(tmp0.getCelsius())
    
import pylab
import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import datetime

array_1 = [23.75, 23.75, 23.75, 23.75, 23.75, 23.75, 23.75, 23.75, 23.75, 23.812, 23.75, 23.812, 23.812, 23.812, 23.812, 23.812, 23.75, 23.75, 23.75, 23.812]
array_2 = [24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24., 24.]

plt.hist(array_1, bins=5, range=[23.75,24.])
plt.hist(array_2, bins=5, range=[23.75,24.])
plt.title('Histogram of 2 datasets')
plt.show()