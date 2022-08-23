"""
Ex 28.

Program Description: The objective of this program is to create a function called “rand_calc” which will randomly generate calculations that the “super_calc” will do (using numbers between 1 and 100.) It will also take in the operation and return a list of answers for each calculator.

"""

import random

class super_calculator:
  calc_list = []

  def __init__(self, x):
    for i in range(x):
      self.calc_list.append(calculator())
  
  def rand_calc(self, op):
    out_list = []
    for x in self.calc_list:
      out_list.append(x.calculate(random.randint(1,100),random.randint(1,100),op))
    return out_list


class calculator:
  num1 = 0.0
  num2 = 0.0
  op = ""

  def __init__(self):
    return
  
  def input(self, n1, n2, op):
    self.num1 = n1
    self.num2 = n2
    self.op = op
    return
  
  def output(self):
    if(self.op == "+"):
      return self.num1 + self.num2
    elif(self.op == "-"):
      return self.num1 - self.num2
    elif(self.op == "*"):
      return self.num1 * self.num2
    elif(self.op == "/"):
      return self.num1 / self.num2
    else:
      return 0
  
  def calculate(self, n1, n2, op):
    self.input(n1, n2, op)
    return self.output()
  

c1 = super_calculator(43)
print(c1.rand_calc("*"))
  
