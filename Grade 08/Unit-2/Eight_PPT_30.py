"""
Ex 30.
Add labels to the X and Y axes of the previous graph'

Program descriptions : The objective of this program is to add labels to the X and Y axes of the previous graph as such.

"""

import matplotlib.pyplot as plt
import numpy as np

plt.xlabel("Student Number")
plt.ylabel("GPA")

points = [3.0, 4.0, 2.5, 3.67, 2.0]

length = len(points)

for i in range(length):
  plt.scatter(i + 1, points[i])

X = [i + 1 for i in range(length)]
Y = points

plt.plot(X, Y)

plt.show
