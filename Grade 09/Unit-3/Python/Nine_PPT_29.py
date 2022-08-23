"""
Ex 29.

Program Description: The objective of this program is to create a list called “ans_list[]” which stores the answers from the “rand_calc” function. Then, create another function “average()” which calculates the average of the dataset.

"""

import random

class super_calculator:
  calc_list = []
  ans_list = []

  def __init__(self, x):
    for i in range(x):
      self.calc_list.append(calculator())
  
  def rand_calc(self, op):
    out_list = []
    for x in self.calc_list:
      out_list.append(x.calculate(random.randint(1,100),random.randint(1,100),op))
    self.ans_list = out_list
    return out_list
  
  def average(self):
    total = 0
    for x in self.ans_list:
      total = total + x
    return total/len(self.ans_list)


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
c1.rand_calc("/")
print(c1.average())
  
