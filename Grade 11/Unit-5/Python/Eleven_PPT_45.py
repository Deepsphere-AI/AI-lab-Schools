"""
Ex. 45

Finally, using scipy's curve_fit, plot the line of best fit in the display function. It can be linear, polynomial or other.
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

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
    def objective(x, a, b, c):
	    return a*(b**x) + c
    plt.scatter(self.x_arr, self.y_arr)
    x, y = self.x_arr, self.y_arr
    popt, _ = curve_fit(objective, x, y)
    a, b, c = popt
    x_line = np.arange(min(x), max(x), 1)
    y_line = objective(x_line, a, b, c)
    plt.plot(x_line, y_line, '--', color='red')
    plt.show()
  

d1 = Data_Analyzer("homes")
d1.default()
d1.display()