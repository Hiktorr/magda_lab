# from scipy import linspace , cos , exp, random, meshgrid, zeros
# from scipy.optimize import fmin
# from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
# def f(x):
#     x1 = x[0]
#     x2 = x[1]
#     f = (4 - 2.1 * (x1 * x1) + (x1 * x1 * x1 * x1) / 3.0) * (x1 * x1) + x1 * x2 + (-4 + 4 * (x2 * x2)) * (x2 * x2)
#     return f
#
# def neg_f(x):
#     return -f(x)
#
# x0 = random.randn(2)
# x_min = fmin(f, x0) #minimum
#
#
#
#
# from mpl_toolkits.mplot3d import Axes3D
#
# delta = 3
# x_knots = linspace(x_min[0] - delta, x_min[0] + delta, 41)
# y_knots = linspace(x_min[1] - delta, x_min[1] + delta, 41)
# X, Y = meshgrid(x_knots, y_knots)
# Z = zeros(X.shape)
# for i in range(Z.shape[0]):
#     for j in range(Z.shape[1]):
#         Z[i][j] = f([X[i, j], Y[i, j]])
#
# ax = Axes3D(figure(figsize=(8, 5)))
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
# ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')
# ax.plot([x_min[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final')
# ax.legend()
# show()

from scipy import linspace , cos , exp, random, meshgrid, zeros
from scipy.optimize import fmin
from matplotlib.pyplot import plot, show, legend, figure, cm, contour, clabel
import time

def f(x):
    x1 = x[0]
    x2 = x[1]
    f = (4 - 2.1 * (x1 * x1) + (x1 * x1 * x1 * x1) / 3.0) * (x1 * x1) + x1 * x2 + (-4 + 4 * (x2 * x2)) * (x2 * x2)
    return f

def neg_f(x):
    return -f(x)

def unique(list1):
    unique_list = []
    count_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
            count_list.append(1)
        else:
            count_list[unique_list.index(x)] += 1
    return unique_list, count_list

resultList = []

currentTime = time.perf_counter()

while time.perf_counter() - currentTime < 5:
    x0 = random.randn(2)
    x_min = fmin(f, x0) #minimum
    resultList.append([round(x_min[0],2),round(x_min[1],2)])

val_list, count_list = unique(resultList)

best_probability = 0
for i in val_list:
    print("Point: {}  |  Value: {}   |  Probability: {}".format(i,f(i),count_list[val_list.index(i)]/sum(count_list)*100))
    if best_probability <= count_list[val_list.index(i)]/sum(count_list)*100:
        best_point = i
        best_probability = count_list[val_list.index(i)]/sum(count_list)*100

print("Plot for point:",best_point)
from mpl_toolkits.mplot3d import Axes3D

delta = 10
x_knots = linspace(best_point[0] - delta, best_point[0] + delta, 41)
y_knots = linspace(best_point[1] - delta, best_point[1] + delta, 41)
X, Y = meshgrid(x_knots, y_knots)
Z = zeros(X.shape)
for i in range(Z.shape[0]):
    for j in range(Z.shape[1]):
        Z[i][j] = f([X[i, j], Y[i, j]])

ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
ax.plot([x0[0]], [x0[1]], [f(x0)], color='g', marker='o', markersize=5, label='initial')
ax.plot([best_point[0]], [x_min[1]], [f(x_min)], color='k', marker='o', markersize=5, label='final')
ax.legend()
show()