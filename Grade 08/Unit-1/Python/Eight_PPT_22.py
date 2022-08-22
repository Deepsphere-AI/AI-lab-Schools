"""
Ex 22.

Program Description: The objective of this program is to create two functions that will allow the user to withdraw or deposit money into the bank account (from the class in the previous program.)

Note: The input will be taken as an integer
"""

import random

class bank_account:
  vAR_balance = 0
  vAR_id_number = 0

  def __init__(self, vAR_num):
    self.balance = vAR_num
    self.id_number = random.randrange(100000,999999)

  def withdraw(self, vAR_num):
    self.balance = self.balance - vAR_num
    return self.balance
  
  def deposit(self, vAR_num):
    self.balance = self.balance + vAR_num
    return self.balance
