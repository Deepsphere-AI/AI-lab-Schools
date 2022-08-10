"""
Ex 42.

Create a class classroom. create the variables class_size, student_list,average_age, and id_range. Give them default values. 
Create the constructor which takes in a number for the classroom size and uses that to create a list of students with the name "Mark",
a random 6- digit id number and either the age 14 or 15.


Program description: The objective of this code is to create a Class Classroom with the following characteristics:
-	Variables: class_size, student_list,average_age, and id_range
-	Give them default values. 
-	Create a constructor which takes in a number for the classroom size and uses that to create a list of students with the name "Mark", a random 6- digit id number and either the age 14 or 15.

Note: Use a loop for the last charcateristics and the random in-built function


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
  average_age = 0
  id_range = 0

  def __init__(self, size):
    self.class_size = size
    for x in range(size):
      self.student_list.append(Student("Mark",random.randrange(100000,999999),random.randrange(14,15)))
