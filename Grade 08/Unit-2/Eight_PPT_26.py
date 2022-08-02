"""
Ex 26.
Plot a line from (1,1) to (8, 8)

Program Description: The objective of this program is to plot a line from the point (1,1) to the point (8, 8) using matplotlib & numpy.

"""
import matplotlib.pyplot as plt
import numpy as np

x = range(1, 9)
y = [i for i in x]

plt.plot(x, y)
plt.show
