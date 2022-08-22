"""
Ex 46.

Using the same code from Ex. 45, round each number to 3 decimal places.

Program Description: The objective of this program is to create an array with random number and specified number of rows and columns (same as Ex. 45) but with rounded to a specified number of decimal places.
Note: Use format np.set_printoptions(precision = x) where x is a number. 

"""
import numpy as np

rand_arr = np.random.random([4,6])
np.set_printoptions(precision=3)

print(rand_arr)
