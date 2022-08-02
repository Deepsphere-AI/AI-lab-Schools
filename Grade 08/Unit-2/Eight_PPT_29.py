"""
Ex 29.
Plot this data with lines connecting each of the points.
ex- (Student, GPA) --> (1, 3.0) ; (2, 4.0) ; (3, 2.5) ; (4, 3.67) ; (5, 2.0)

Program description : The objective of this program is to plot this data with lines connecting each of the points.

"""
import matplotlib.pyplot as plt
import numpy as np

points = [3.0, 4.0, 2.5, 3.67, 2.0]

length = len(points)

for i in range(length):
  plt.scatter(i + 1, points[i])

X = [i + 1 for i in range(length)]
Y = points

plt.plot(X, Y)
plt.show
