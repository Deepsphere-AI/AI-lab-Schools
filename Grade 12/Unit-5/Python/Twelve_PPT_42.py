 """
Ex. 42

Create a constructor for the function.
"""

import numpy as np

class Data_Plotter:
  type = ""
  X = np.array([])
  Y = np.array([])

  def __init__(self, type, x, y):
    self.type = type
    self.X = x
    self.Y = y

dp1 = Data_Plotter("Bar", ["A", "B", "C", "D"], [20,43,56,12])