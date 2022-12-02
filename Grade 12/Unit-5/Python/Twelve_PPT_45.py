"""
Ex. 45

Create a function pie that plots a pie chart with the Y values.
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
  
  def pie(self):
    plt.pie(self.Y)

dp1 = Data_Plotter("Bar", ["A", "B", "C", "D"], [43,23,27,7])
dp1.pie()