"""
Ex. 49

Create the function random which will return an array of x randomly assigned numbers from a given range.
"""

import numpy as np
import matplotlib.pyplot as plt
import random

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
  
  def plot(self):
    if(self.type.lower()== "bar"):
      self.bar()
    elif(self.type.lower()== "line"):
      self.line()
    elif(self.type.lower()== "pie"):
      self.pie()
    else:
      self.hist()
  
  def change_type(self, type):
    self.type = type
  
  def random(self,x, lower,upper):
    arr = []
    for i in range(x):
      arr.append(random.randrange(lower,upper))
    return arr
    

dp1 = Data_Plotter("Line", [1,2,3,4], [43,23,27,7])
dp1.plot()
dp1.change_type("Bar")
dp1.plot()
print(dp1.random(10,0,10))