"""
Ex 44.

Using the Classroom class from the previous excercise, create a function calc_id_range which will calculate the range of the ids.
This means that it will set the self.id_range to the highest id minus the lowest id. For example, if a student had an id of 999999,
and it was the highest, and another student had an id of 100000, and it was the lowest, the id_range would be 999999-100000 = 899999.


Program description: The objective of this code is to create a function to find the range of the ids. We first use a for loop to find the 
min and max values and then use them to find the range and then return it.
Note: Create local variables only for the newly created function for min and max values.


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

  def calc_id_range(self):
    min = 999999
    max = 0
    for x in self.student_list:
      if(x.get_id() > max):
        max = x.get_id()
      elif(x.get_id() < min):
        min = x.get_id()
    self.id_range = max - min
    return self.id_range




me = Classroom(20)
print(me.calc_id_range())
