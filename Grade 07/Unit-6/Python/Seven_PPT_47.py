"""
Ex 47.

Add to the bank_account class 2 functions, withdraw and despoit, which will take in a integer input and add/subtract the the balance the corresponding amount.

Program description: The objective of this code is the create 2 new functions to the bank_account class.
The first one is called withdraw which will take in an integer input and subtract it from the balance. 
The second is called deposit and will again take in an integer input and add it to the existing balance.
Thus, they change the values of the balance attributes.
"""

import random

class bank_account:
  balance = 0
  id_number = 0

  def __init__(self, num):
    self.balance = num
    self.id_number = random.randrange(100000,999999)

  def withdraw(self, num):
    self.balance = self.balance - num
    return self.balance
  
  def deposit(self, num):
    self.balance = self.balance + num
    return self.balance
