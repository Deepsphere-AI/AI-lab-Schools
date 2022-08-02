"""
Ex. 32

Create a constructor which takes in a name and sets it equal to the class's name variable, but adds .csv to the name passed in. Ie, Data_Analyzer("homes") should set the name value to "homes.csv"
"""

class Data_Analyzer:
  name = ""
  columns = []

  def __init__(self,name):
    self.name = name + ".csv"

d1 = Data_Analyzer("homes")