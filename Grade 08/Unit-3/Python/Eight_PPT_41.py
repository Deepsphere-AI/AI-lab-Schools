"""
Ex 41.

Given the array, arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), extract all odd numbers from the array.

Program Description: The objective of this program is to extract all odd numbers from a given array. We use numpy to do the same. We enter the Boolean condition for choosing all odd numbers.
Note: We have done the same program before using for loops or while loops, however, that uses more lines of code, this is more efficient.

"""

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr[arr % 2 == 1]

print(arr)
