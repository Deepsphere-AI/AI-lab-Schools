"""
Ex 31.
Add a title to the previous graph.

Program descriptions : The objective of this program is to add a title to the previous graph

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

plt.title("Student Grades")

plt.plot(X, Y)
