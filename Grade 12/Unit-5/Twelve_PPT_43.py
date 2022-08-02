"""
Ex. 43

Create a function bar which will use matplotlib and graph the function as a bar graph with the X and Y values
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

dp1 = Data_Plotter("Bar", ["A", "B", "C", "D"], [20,43,56,12])
dp1.bar()