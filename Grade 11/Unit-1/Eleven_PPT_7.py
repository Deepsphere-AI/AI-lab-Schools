""""
Ex. 7

Create a class student. It should have a constructor with __init__(self,...) and the variables name, id_number, and age. There should also be functions to get these values and return them.
"""

class Student:
  name = ""
  id_number = 0
  age = 0

  def __init__(self, name, id_number, age):
    self.name = name
    self.id_number = id_number
    self.age = age
  
  def get_name(self):
    return self.name
  
  def get_id(self):
    return self.id_number

  def get_age(self):
    return self.age


