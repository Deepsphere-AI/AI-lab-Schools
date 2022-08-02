"""
Ex. 42

Create a constructor which takes in a string, adds ".csv" to it and sets it equal to self.name.
"""

class Data_Analyzer:
  name = ""
  x_arr = []
  y_arr = []

  def __init__(self, name):
    self.name = name + ".csv"