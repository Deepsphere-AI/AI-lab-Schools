"""
Ex. 37

Create a function get_columns that will just open the csv function as a csv file for and take the first row and set each variable to a corresponing place in self.columns.
"""

import csv

class Data_Analyzer:
  name = ""
  columns = []

  def __init__(self,name):
    self.name = name + ".csv"

  def get_columns(self):
    with open(self.name) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
            self.columns = row
            line_count+=1
    return self.columns

d1 = Data_Analyzer("homes")
print(d1.get_columns())