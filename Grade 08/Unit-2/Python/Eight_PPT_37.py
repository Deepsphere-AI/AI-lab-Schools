"""
Ex 37.

Generate 100 random x values (mean of 150 with standard deviation of 10) using np.random.normal() to make sure that we can create a normal histogram with them.

Program description: The objective of this program is to generate 100 random x values (mean of 150 with standard deviation of 10) using np.random.normal() to make sure that we can create a normal Histogram with them.

"""
import numpy as np

x = np.random.normal(150, 10, 100)

print(x)
