"""
Ex 23.

Program Description: The objective of this program is to create a function which inputs 2 numbers and a arithmetic operation ( + , - , * , / ). Then set the self variables to one passed in.

"""

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
