# TASKS (9p)
# 1 Looking at the Euler method above create your own function which takes:
# a (from x' = ax)
# h - step
# T time range
# as an input and plots the solution of a differential equation x' = ax (1p)
# 2 Beside the solution print the 'ideal' approximation on your chart using for example green color as a reference. (1p)
# 2 Hint: use small step value. Use plt.legend to explain which serie is the 'ideal'
# 3 Find a differential equation which represents a process / model (your choice) and implement it using odeint python function (1p)
# 4 Look at the example of optimization for exponential function.
# Did you encounter any errors? Where in code do we display the optimal point? Do we minimize or maximize and which function?
# Start your search always from the point (0, -2). (1p)
# 5 Create your own 3d function with multiple local optima.
# Create an algorithm which takes an initial point and looks for the closest local optimum (1p)
# Create an algorithm which aims to find a global optimum, the time of execution is limiter to ~30sec (1p)
# If your solution is heuristic test its quality. Measure the probability of finding the GLOBAL optimum (1p).
# You can, for example, execute your search function multiple times and check if the returned result is what you expected.
# Measure the success / total trials rate (2p).

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def eulerMethod(a,h,T):
    initial_x = 1

    t = np.arange(0, T, h)
    x = np.zeros(t.shape)
    x[0] = initial_x


    t_ideal = np.arange(0, T, 0.001)
    x_ideal = np.zeros(t_ideal.shape)
    x_ideal[0] = initial_x

    for i in range(t.size - 1):
        x[i + 1] = x[i] + h * (a * x[i])

    for i in range(t_ideal.size - 1):
        x_ideal[i+1] = x_ideal[i] + 0.001 * (a * x_ideal[i])

    plt.plot(t, x, 'o', t_ideal, x_ideal, 'g.')
    plt.legend(['Euler Method','Ideal solution'])
    plt.xlabel('t', fontsize=14)
    plt.ylabel('x', fontsize=14)
    plt.show()

eulerMethod(2,0.1,5)

# def F(x,t):
#     dx = -x + 1.0
#     return dx
#
# # initial condition
# initial_x = 0
#
# t_min = 0
# t_max = 50
# h = 0.01
# t = np.arange(t_min, t_max+h, h)
#
# # solve ODE
# X = odeint(F,initial_x,t)
#
# # plot results
# plt.plot(t,X)
# plt.xlabel('time')
# plt.ylabel('y(t)')
# plt.show()

