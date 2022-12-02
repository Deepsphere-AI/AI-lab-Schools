"""""
Ex. 16

Create a scatter plot with the tables: x_val = [5,7,8,7,2,17,2,9,4,11,12,9,6] and y_val = [99,86,87,88,111,86,103,87,94,78,77,85,86]
"""

import numpy as np
import random
import matplotlib.pyplot as plt

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

y = np.random.triangular (1,50, 100, 250000)

x_val = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y_val = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x_val, y_val)
plt.show()