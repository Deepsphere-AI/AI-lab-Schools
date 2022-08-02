"""
Ex 44.

Create the function randomize that will take in x and create 10 random points and add them to x and y. Make the range between 1 and 100.
"""

import random

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


l1 = Line_Plotter()
l1.points([ "2,3" , "2,4" , "2,5" , "2,6"])
l1.randomize(10)
