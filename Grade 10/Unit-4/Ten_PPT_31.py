"""
Ex 31.

Create an array with np.array called speed and give it 13 random values from 60 to 120.
"""

import numpy as np
import random

speed = np.array([])

for x in range(13):
  speed = np.append(speed,random.randint(60,120))

print(speed)