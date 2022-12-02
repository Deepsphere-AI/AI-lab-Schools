"""""
Ex. 13

Using np.std, find and print the standard deviation of this array.
"""

import numpy as np
import random

speed = np.array([])

for x in range(13):
  speed = np.append(speed,random.randint(60,120))

mean = np.mean(speed)
std = np.std(speed)

print(speed)
print(mean)
print(std)