"""
Ex. 44

Using matplotlib, create a function display which will plot the x and y points.
"""

import csv
import matplotlib.pyplot as plt


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

  def display(self):
    plt.scatter(self.x_arr, self.y_arr)
    plt.show()

d1 = Data_Analyzer("homes")
d1.default()
d1.display()