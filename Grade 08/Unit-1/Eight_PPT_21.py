"""
Ex 21.

Program Description: The objective of this program is to create a bank account class which will ask for the balance and generate a random id.

"""

import random

class bank_account:
  vAR_balance = 0
  vAR_id_number = 0

  def __init__(self, vAR_num):
    self.balance = vAR_num
    self.id_number = random.randrange(100000,999999)
