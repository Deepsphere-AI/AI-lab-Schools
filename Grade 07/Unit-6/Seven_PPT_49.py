"""
Ex 49.

Finally, edit the withdraw and deposit functions in the bank account class to include verify. Only do the transaction if the verification is true.

Program description: The objective of this function is to edit the withdraw and deposit functions (47) to ensure that the transaction only
takes place of the verify function is true.
"""

import random

class bank_account:
  balance = 0
  id_number = 0

  def __init__(self, num):
    self.balance = num
    self.id_number = random.randrange(100000,999999)

  def withdraw(self, num):
    if(self.verify()):
      self.balance = self.balance - num
    return self.balance
  
  def deposit(self, num):
    if(self.verify()):
      self.balance = self.balance + num
    return self.balance
  
  def verify(self):
    return self.id_number == int(input("What is your id_number?"))
  
  def get_id_num(self):
    return self.id_number
