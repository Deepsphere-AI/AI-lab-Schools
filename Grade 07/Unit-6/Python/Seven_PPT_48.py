"""
Ex 48.

Add to the bank_account class a function called verify, which will take in user input using input(), 
and check and see if the id_numbers match return a boolean corresponding to whether they match or not

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
  
  def verify(self):
    return self.id_number == int(input("What is your id_number?"))
  
  def get_id_num(self):
    return self.id_number
