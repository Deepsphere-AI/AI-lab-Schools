"""
Ex 19.

Program Description: The objective of this program is to create a function which will calculate the average age of the students in the class (from the previous program) and return the value as a float.

Remember: Float means “floating point value,” which is a decimal.
"""

import random

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


class Classroom:
  vAR_class_size = 0
  vAR_student_list = []
  vAR_average_age = 0.0
  vAR_id_range = 0

  def __init__(self, vAR_size):
    self.class_size = vAR_size
    for x in range(vAR_size):
      self.vAR_student_list.append(Student("Mark",random.randrange(100000,999999),random.randrange(14,16)))
  
  def get_average_age(self):
    vAR_total = 0
    for vAR_x in self.vAR_student_list:
      vAR_total = vAR_total + vAR_x.get_age()
    self.vAR_average_age = vAR_total/self.vAR_class_size
    return self.vAR_average_age

me = Classroom(20)
print(me.get_average_age())
