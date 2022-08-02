"""
Ex. 39

Now create the function max which finds the house with the max sell and return the position of the max house.
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

  def display(self,line):
    with open(self.name) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        line_count+=1
        if line_count == line:
          return f'\t Age:{row[6]} , Sell: {row[0]} , Acres {row[7]}.'
  
  def max(self):
    max = 0
    pos = 0
    with open(self.name) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if(line_count != 0):
          if(float(f'{row[0]}') > max):
            max = int(f'\t {row[0]}')
            pos = line_count+1 
        line_count+=1
    return pos

d1 = Data_Analyzer("homes")
print(d1.get_columns())
print(d1.display(d1.max()))
