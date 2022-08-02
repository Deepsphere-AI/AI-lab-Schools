"""
Ex 38.

Create a random histogram with np.random.normal() that is centered around 100 with a standard deviation of 10.

Program Description: The objective of this program is to  create a random histogram with np/random.normal() that is centered around 100 with a standard deviation of 10.

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(100, 10, 250) # The 170 is the mean and the 10 is the standard deviation. We are also using .normal so that our histogram will be relativly normal

plt.hist(x)
