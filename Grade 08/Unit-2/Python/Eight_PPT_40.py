"""
Ex 40.

Create and show a pie chart that has 4 randomized sections.

Program Description: The objective of this program is to create a pie chart that is randomly divided into 4 sections by entering the percentage out of 100 with the random function.
Note: You need to add a range using random.randrange(start, end)

"""

import matplotlib.pyplot as plt
import numpy as np
import random

X = np.array([random.randrange(0,100), random.randrange(0,100), random.randrange(0,100), random.randrange(0,100)])

plt.pie(X)
