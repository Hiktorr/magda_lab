#task 4
#looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)

from sys import argv
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *

y = []
x = int(argv[1])
for i in range(x):
    y.append(i**2)

plot(range(x),y)
show()