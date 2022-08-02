"""
Ex 37.

Create a linear regression model with the given points on a scatter plot. To do this get the data points slope, intercept, r, p,and std_err from stats (import scipy).linregress(x, y). Then graph it with list(map())
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy import stats

speed = np.array([])

for i in range(13):
  speed = np.append(speed,random.randint(60,120))

mean = np.mean(speed)
std = np.std(speed)
pct_75 = np.percentile(speed,75)
pct_99 = np.percentile(speed,99)

print(speed)
print(mean)
print(std)
print(pct_75)
print(pct_99)

y = numpy.random.triangular (1,50, 100, 250000)

x_val = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y_val = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x_val, y_val)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x_val))

plt.scatter(x_val, y_val)
plt.plot(x_val, mymodel)
plt.show()
