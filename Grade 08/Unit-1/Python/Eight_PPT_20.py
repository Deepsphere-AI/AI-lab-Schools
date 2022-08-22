"""
Ex 20.

Program Description: The objective of this program is to create a function which will calculate the range of the id numbers (from programs 18 & 19.)

Note: Range is the difference between the highest and lowest values.

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
    for x in self.vAR_student_list:
      vAR_total = vAR_total + x.get_age()
    self.average_age = vAR_total/self.class_size
    return self.average_age

  def calc_id_range(self):
    min = 999999
    max = 0
    for x in self.vAR_student_list:
      if(x.get_id() > max):
        max = x.get_id()
      elif(x.get_id() < min):
        min = x.get_id()
    self.id_range = max - min
    return self.id_range




me = Classroom(20)
print(me.calc_id_range())
