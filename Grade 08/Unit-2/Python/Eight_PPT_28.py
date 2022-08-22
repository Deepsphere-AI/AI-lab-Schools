"""
Ex 28.
Draw a smiley face using plt.scatter and plt.plot

Program Description: The objective of this program is to draw a smiley face using the functions .scatter() and .plot() in matplotlib.

"""
import matplotlib.pyplot as plt
import numpy as np

eyeY = 40
left = -2
right = 2

X = range (-5, 6)
Y = [i*i for i in X]

plt.scatter(left, eyeY)
plt.scatter(right, eyeY)

plt.plot(X, Y)

plt.show
