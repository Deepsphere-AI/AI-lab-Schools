"""
Ex 28.

Add to the preivous class another variable age and a corresponding function, change_age to change the age.

Program description: The objective of this program is to add to the previous class another variable “age” and a corresponding function and change_age to change the age.
Answer time:
 Now after reading the last 3 exercises some of you might have a doubt that for what is this class used for?
Answer: - Class creates a user-defined data structure, which holds its own data members and members functions, 
which can be accessed and used by creating an instance of that class. A class is an outline, copy or blueprint of that object.

"""

class animal:
  animal_type = ""
  vAR_age = 0

  def change_type(self,vAR_str_in):
    self.animal_type = vAR_str_in

  def change_age(self,vAR_int_in):
    self.vAR_age = int(vAR_int_in)
