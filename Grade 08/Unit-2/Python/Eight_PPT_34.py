"""
Ex 34.
Using the code from ex.33, theres a cool feature with matplotlib that will add grids to the graph. Using the .grid() function, add a grid to the graph.

Program Description: The objective of this program is to use the .grid() function from matplotlib to add a grid to the graph from the previous program.

"""

import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 3])
Y = np.array([1, 2, 3])

plt.grid()

plt.plot(X, Y)
