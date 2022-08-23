"""
Ex 16.

Create the function line that plots a line graph with the X and Y values as the corresponding X and Y values.
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
  
  def line(self):
    plt.plot(self.X,self.Y)

dp1 = Data_Plotter("Bar", [1,2,3,4], [43,23,27,7])
dp1.line()