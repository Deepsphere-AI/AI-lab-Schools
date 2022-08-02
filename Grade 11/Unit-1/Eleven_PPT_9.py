""""
Ex. 9

Using the Classroom class from the previous excercise, create a function, get_average, which will calculate the average age of the students, set that equal to self.average_age, and return it as a float (floating point number).
"""

import random

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


class Classroom:
  class_size = 0
  student_list = []
  average_age = 0.0
  id_range = 0

  def __init__(self, size):
    self.class_size = size
    for x in range(size):
      self.student_list.append(Student("Mark",random.randrange(100000,999999),random.randrange(14,16)))
  
  def get_average_age(self):
    total = 0
    for x in self.student_list:
      total = total + x.get_age()
    self.average_age = total/self.class_size
    return self.average_age

me = Classroom(20)
print(me.get_average_age())