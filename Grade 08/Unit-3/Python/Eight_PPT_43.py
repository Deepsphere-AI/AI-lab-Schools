"""
Ex 43.

Given the arrays, arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) and arr1 = np.array([2, 3, 4]), find the common items present in both arrays.

Program Description: The objective of this program is to find the common items between two arrays using numpy. The common items get added to a new array.
Note: Use the format np.intersec1d(arr1, arr2) to find the common items.

"""

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr1 = np.array([2, 3, 4])

arr2 = np.intersect1d(arr,arr1)

print(arr2)
