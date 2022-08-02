"""
Ex 39.

Create and show a pie chart that has 4 equal sections.

Program Description: The objective of this program is to create a pie chart that is equally divided into 4 sections by entering the percentage out of 100 for each part. 

"""

import matplotlib.pyplot as plt
import numpy as np

X = np.array([25, 25, 25, 25])

plt.pie(X)
