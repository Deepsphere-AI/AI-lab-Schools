"""
Ex 33.

Add to the Calculator class a function that will add the 2 numbers.

Program description: The objective of this program is to add a function to the Calculator Class that will add 2 numbers.
Here the Class has 3 attributes that are edited in the first function and the final answer is returned in the second function.
"""

class Calculator:
   num1 = 0
   num2 = 0
   operation = ""

   def __init__ (self, num1, num2, operation):
     self.num1 = int(num1)
     self.num2 = int(num2)
     self.operation = operation

   def add(self):
     return self.num1+self.num2
