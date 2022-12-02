"""
Ex. 34 

Create a function Most_Expensive() which will details of the most expensive house.
"""

import pandas as pd

class Data_Analyzer:
  name = ""
  columns = []

  def __init__(self,name):
    self.name = name + ".csv"
  
  def open(self):
    return pd.read_csv(self.name)

  def Most_Expensive(self):
    return max(open(self.name)) 

d1 = Data_Analyzer("homes")
print(d1.open())
print(d1.Most_Expensive())