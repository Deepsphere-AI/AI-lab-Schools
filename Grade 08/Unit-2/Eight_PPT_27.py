"""
Ex 27.
Plot the parabola y = x^2 + 6x + 9 from x = -10 to x = 10

Program Description: The objective of this program is to plot the equation of the parabola (y = x^2 + 6x + 9) from the x values -10 and 10.
"""
import matplotlib.pyplot as plt
import numpy as np

x = range(-10, 11)
y = [(i*i + 6*i + 9) for i in x]

plt.plot(x, y)
plt.show
