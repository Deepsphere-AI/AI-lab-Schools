"""
Ex. 33

Import pandas. Create a function open which will use pandas.read_csv to open a csv and return it. Then create a variable called csv at the top which will hold the output of pandas_read_csv.
"""

import pandas as pd

class Data_Analyzer:
  name = ""
  columns = []

  def __init__(self,name):
    self.name = name + ".csv"
  
  def open(self):
    return pd.read_csv(self.name)

d1 = Data_Analyzer("homes")
print(d1.open())