"""
Ex 17.

Program Desciption: The objective of this program is to create a class student. It should utilize the constructor with __init__(self,...) and the variables name, id_number, and age. Create functions to get the value and return them.

"""

class Student:
  vAR_name = ""
  vAR_id_number = 0
  vAR_age = 0 

  def __init__(self, vAR_name, vAR_id_number, vAR_age):
    self.name = vAR_name
    self.id_number = vAR_id_number
    self.age = vAR_age
  
  def get_name(self):
    return self.name
  
  def get_id(self):
    return self.id_number

  def get_age(self):
    return self.age
