"""
Ex 45.

Create a random array with floats from 0 to 1. Give this array 4 rows and 6 columns.

Program Description: The objective of this program is to create an array with random numbers and specified number of rows and column. 
Note: Use format np.random.random([rows, columns])

"""

import numpy as np

rand_arr = np.random.random([4,6])

print(rand_arr)
