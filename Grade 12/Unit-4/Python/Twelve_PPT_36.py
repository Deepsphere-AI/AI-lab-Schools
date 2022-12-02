"""
Ex. 36

Now let's try and read a csv with the csv module in python. Create the same class as before with the same variabels and constructor (excluding the functions), and import csv.
"""

import csv

class Data_Analyzer:
  name = ""
  columns = []

  def __init__(self,name):
    self.name = name + ".csv"

d1 = Data_Analyzer("homes")