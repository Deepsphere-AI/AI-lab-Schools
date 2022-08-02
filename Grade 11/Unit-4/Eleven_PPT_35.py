"""
Ex. 35

Create a function Least_Expensive() which will details of the least expensive house.
"""

import pandas as pd
import numpy as np

class Data_Analyzer:
  name = ""
  columns = []

  def __init__(self,name):
    self.name = name + ".csv"
  
  def open(self):
    return pd.read_csv(self.name)

  def Most_Expensive(self):
    return max(open(self.name)) 
  
  def Least_Expensive(self):
    return min(open(self.name)) 

d1 = Data_Analyzer("homes")
print(d1.open())
print(d1.Most_Expensive())
print(d1.Least_Expensive())