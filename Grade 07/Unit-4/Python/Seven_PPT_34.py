"""
Ex 34.

Add to the Calculator class a function that will add the subtract the 2 numbers, one that will divide, and one that will multiply

Program description: The objective of this program is to add 3 functions to the Calculator Class that will subtract, 
multiply, and divide apart from the already existing add function (Ex  33). 
Note: Doesn’t the Calculator Class now resemble a 4-function Calculator?

"""

class Calculator:
   vAR_num1 = 0
   vAR_num2 = 0
   vAR_operation = ""

   def __init__ (self, vAR_num1, vAR_num2, vAR_operation):
     self.vAR_num1 = int(vAR_num1)
     self.vAR_num2 = int(vAR_num2)
     self.vAR_operation = vAR_operation

   def add(self):
     return self.vAR_num1+self.vAR_num2

   def subtract(self):
     return self.vAR_num1-self.vAR_num2

   def multiply(self):
     return self.vAR_num1*self.vAR_num2

   def divide(self):
     return self.vAR_num1/self.vAR_num2
