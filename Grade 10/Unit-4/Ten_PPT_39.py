"""
Ex 39.

Create a new plot of 10 x and y values completely randomized from 1 to 100.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import random

x = []
y = []

for i in range(10):
  x = np.append(x,[random.randint(1,100)])

for j in range(10):
  y = np.append(y,[random.randint(1,100)])
plt.scatter(x, y)
plt.show()