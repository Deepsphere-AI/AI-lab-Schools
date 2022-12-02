"""""
Ex. 12

Using np.mean, find and print the mean of this array.
"""

import numpy as np
import random

speed = np.array([])

for x in range(13):
  speed = np.append(speed,random.randint(60,120))

mean = np.mean(speed)

print(speed)
print(mean)