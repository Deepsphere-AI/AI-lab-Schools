"""
Ex 24.

Program Description: The objective of this program is to add verification to the withdraw and deposit functions.

Note: Only do the transaction if the verification returns “True.”

"""

import random

class bank_account:
  vAR_balance = 0
  vAR_id_number = 0

  def __init__(self, vAR_num):
    self.balance = vAR_num
    self.id_number = random.randrange(100000,999999)

  def withdraw(self, vAR_num):
    if(self.verify()):
      self.balance = self.balance - vAR_num
    return self.balance
  
  def deposit(self, vAR_num):
    if(self.verify()):
      self.balance = self.balance + vAR_num
    return self.balance
  
  def verify(self):
    return self.id_number == int(input("What is your id_number?"))
  
  def get_id_num(self):
    return self.id_number
