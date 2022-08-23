"""
Ex 27.

Program Description: The objective of this program is to create and add a constructor which will take in a variable called “x” and add “x” number of calculators to the list.

"""

class super_calculator:
  calc_list = []

  def __init__(self, x):
    for i in range(x):
      self.calc_list.append(calculator())


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
  
