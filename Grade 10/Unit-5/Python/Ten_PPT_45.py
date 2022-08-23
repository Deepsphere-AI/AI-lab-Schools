"""
Ex 45.

Create the function myfunc() as before in order to plot a line of best fit for the points.
"""

import random
from scipy import stats

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

  def myfunc(self,x):
    slope, intercept, r, p, std_err = stats.linregress(self.x_list, self.y_list)
    return slope * self.x + intercept


l1 = Line_Plotter()
l1.points([ "2,3" , "2,4" , "2,5" , "2,6"])
l1.randomize(10)
