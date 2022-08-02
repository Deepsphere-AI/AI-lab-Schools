"""
Ex 36.

Now Using the random class in python, create a bar chart with 4 categories, "A" through "D", but randomize each value from 1 to 20.

Program Description: The objective of this program is to use a random class  in python and create a bar chart with 4 categories, “A” through “D” , but randomize each value from 1 to 20. This program highlights the usage of “randrange”. 

"""

import numpy as np
import matplotlib.pyplot as plt
import random

X = np.array(["A", "B", "C", "D"])
Y = []
for x in range(0,4):
  Y.append(random.randrange(1,21))


plt.bar(X, Y)
