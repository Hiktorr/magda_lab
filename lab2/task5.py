import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sys import argv

inputNumber = float(argv[1])
if inputNumber == 0:
    print("Input number cannot be 0, changed to 1")
    inputNumber = 1
x_knots = np.linspace(-3*np.pi/inputNumber,3*np.pi*inputNumber,201)
y_knots = np.linspace(-3*np.pi/3*inputNumber,3*np.pi,201)
X, Y = np.meshgrid(x_knots, y_knots)
R = np.sqrt(X**2+Y**2)
Z = np.cos(R)**2*np.exp(-0.1*R)
ax = Axes3D(plt.figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)
plt.show()