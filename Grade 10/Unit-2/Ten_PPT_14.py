"""
Ex 14.

Create a function hist that creates a histogram with the Y Values.
"""

import numpy as np
import matplotlib.pyplot as plt

class Data_Plotter:
  type = ""
  X = np.array([])
  Y = np.array([])

  def __init__(self, type, x, y):
    self.type = type
    self.X = x
    self.Y = y
  
  def bar(self):
    plt.bar(self.X, self.Y)
  
  def hist(self):
    plt.hist(self.Y)

dp1 = Data_Plotter("Bar", ["A", "B", "C", "D"], [1,1,2,3,3,3,3,3,3,4,4,4,4,4,5,5,6,7,8,8,9,9,9,10])
dp1.hist()