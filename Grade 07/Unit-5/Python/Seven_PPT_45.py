"""
Ex 45.

Using the Classroom class from the previous excercise, find how many students are 14, and how many are 15 years old.
Then add up all the ages of 15s, and 14s seperatly. Then find the difference to see how many years apart the total class is.

Program description: 
                   The objective of this code is to create a function to find out how many students are 14, and how many are 15 years old. 
                   Then it will add up all the ages of 15s, and 14s separately.
                   Then it will find the difference and return it to see how many years apart the total class is.
                   
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
  
  def years_apart(self):
    fourteen = 0
    fifteen = 0
    for x in self.student_list: 
      if(x.get_age() == 14):
        fourteen +=14
      else:
        fifteen+=15
    return fifteen - fourteen




me = Classroom(20)
print(me.years_apart())
