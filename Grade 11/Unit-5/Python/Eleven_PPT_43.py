"""
Ex. 43

Create a function default that will set the x_arr to the values in column 6, and the y_arr to the values in column 0.
"""

import csv

class Data_Analyzer:
  name = ""
  x_arr = []
  y_arr = []

  def __init__(self, name):
    self.name = name + ".csv"
  
  def default(self):
    with open(self.name) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if(line_count == 0):
          line_count+=1
          continue
        self.x_arr.append(int(f'\t {row[6]}'))
        self.y_arr.append(int(f'\t {row[0]}'))
        line_count+=1
d1 = Data_Analyzer("homes")
d1.default()