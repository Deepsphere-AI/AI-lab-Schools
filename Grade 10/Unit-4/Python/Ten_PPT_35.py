"""
Ex 35.

Create an array with a triangular distribution with a length of 250,a mode of 50, and containing values between 1 and 100. Then using matoplotlib, display a histogram with 10 bins.
"""

import numpy as np
import random
import matplotlib.pyplot as plt

y = numpy.random.triangular (1,50, 100, 250000)

speed = np.array([])

for x in range(13):
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

plt.hist(y, 10)
plt.show()