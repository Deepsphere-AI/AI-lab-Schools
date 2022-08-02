"""
Ex 42.

Given the array, arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), arrange it so that the first half of the array is on top when printed and the other half is on the bottom

Program Description: The objective of this program is to arrange an array in such a way that the first half is on top and the other on bottom when it gets printed. You utilize arr.reshape and enter the rows and columns as the criterion for this to happen using numpy. 
Note: Use this format arrName.reshape(rows, columns), when you enter -1 in columns, it makes it such that, the number of columns depends automatically on the number of rows and how the array is split.

"""

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr = arr.reshape(2, -1) # 2 is rows and -1 is columns. The -1 makes it so that it decides how many columns automatically 

print(arr)
