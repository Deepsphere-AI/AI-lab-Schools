"""
Ex 41.

Create a class student. It should have a constructor with __init__(self,...) and the variables name, id_number, and age.
There should also be functions to get these values and return them.

Program description: The objective of this function is to create a Class based on previous knowledge with the following characteristics.
-	Name: student
-	Constructor: __init__(self,…)
-	Variables: name, id_number, and age
-	There must also be functions to change and get the attributes of the objects.

"""
class Student:
  vAR_name = ""
  vAR_id_number = 0
  vAR_age = 0

  def __init__(self, vAR_name, vAR_id_number, vAR_age):
    self.vAR_name = vAR_name
    self.vAR_id_number = vAR_id_number
    self.vAR_age = vAR_age
  
  def get_name(self):
    return self.vAR_name
  
  def get_id(self):
    return self.vAR_id_number

  def get_age(self):
    return self.vAR_age
