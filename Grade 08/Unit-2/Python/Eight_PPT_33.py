"""
Ex 33.
Using the array created in ex 32, create another array and plot the points as a line.

Program Description: The objective of this program is to create another array (using the array from the previous program) and plot the points as a line.

"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

plt.plot(X, Y)
