"""
Ex 43.

Create the function points that given a list of points 92,3) seperated by commas, it will add each point to the corresponding x and y lists. An example list would be [ 2,3 , 2,4 , 2,5 , 2,6]
"""

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

l1 = Line_Plotter()
l1.points([ "2,3" , "2,4" , "2,5" , "2,6"])
