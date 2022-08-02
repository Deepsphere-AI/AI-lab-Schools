"""
Ex 40.

Now apply linear regression to the x and y model just created.
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

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)

plt.show()