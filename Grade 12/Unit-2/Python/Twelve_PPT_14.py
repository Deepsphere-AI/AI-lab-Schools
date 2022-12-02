"""""
Using np.precentiles, find and print 75th and 99th percentile of the speeds.
"""

import numpy as np
import random

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