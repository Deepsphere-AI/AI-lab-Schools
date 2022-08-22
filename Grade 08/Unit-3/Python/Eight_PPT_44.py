"""
Ex 44.

Given the arrays, arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) and arr1 = np.array([2, 3, 4]), find the common items present in both arrays and delete them from the arr.

Program Description: The objective of this program is to find and delete the common items present in two arrays. These common items are put into a new set. 
Note: Use the format np.setdiff1d(arr1, arr2)

"""

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr1 = np.array([2, 4, 8])

arr2 = np.setdiff1d(arr,arr1)

print(arr2)
