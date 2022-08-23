"""
Ex 46.

Now plot the points as well as the line of best fit
"""

import random
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

class Line_Plotter:
  x_list = []
  y_list = []

  def __init__(self):
    return
  
  def points(self, point_list):
    for x in point_list:
      temp = x.split(",")
      self.x_list.append(temp[0])
      self.y_list.append(temp[1])
  
  def randomize(self, x):
    for i in range(x):
      self.x_list.append(random.randint(1,100))
      self.y_list.append(random.randint(1,100))

  def myfunc(x):
    slope, intercept, r, p, std_err = stats.linregress(x_list, y_list)
    return slope * x + intercept
  
  mymodel = list(map(myfunc, x_list))

  plt.scatter(x_list, y_list)
  plt.plot(x_list, mymodel)

  plt.show()  


l1 = Line_Plotter()
l1.points([ "2,3" , "2,4" , "2,5" , "2,6"])
l1.randomize(10)
