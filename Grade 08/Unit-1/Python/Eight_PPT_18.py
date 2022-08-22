"""
Ex 18.

Program Description: The objective of this program is to create a class- classroom. Create the variables for class_size, student_list,average_age, and id_range. Input a few default values. Create a constructor which can take in a number for the classroom size and can use it   to create a list of students with the name "Mark", a random 6- digit id number, and either the age 14 or 15.

Note- Make sure Random is successfully imported for the program to work

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
  vAR_average_age = 0
  vAR_id_range = 0

  def __init__(self, vAR_size):
    self.class_size = vAR_size
    for x in range(vAR_size):
      self.vAR_student_list.append(Student("Mark",random.randrange(100000,999999),random.randrange(14,15)))
