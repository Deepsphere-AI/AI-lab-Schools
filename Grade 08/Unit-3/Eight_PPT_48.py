"""
Ex 48.

Using the code from ex 47, format the output so that only the first and last 3 numbers will be shown.

Program Description: The objective of this program is to create an array counting numbers upto a specific values and format the output so that only the first and last 3 numbers will be shown. 
Note: Use the format np.set_printoptions(threshold=x) where x is the number.

"""

import numpy as np

arr = np.arange(20)
np.set_printoptions(threshold=6)

print(arr)
