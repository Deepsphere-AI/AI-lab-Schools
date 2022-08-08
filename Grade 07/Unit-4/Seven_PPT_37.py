"""
Ex 37.

Using the code for the last excersise, print out the name and age of Fido.

Program description: The objective of this code is to print out the attributes name and age of the object “Fido” 
(this was created in 36) using the functions already part of the given Animal Class.
Note: This is of the format objectName.functionName()

"""

class animal:
   animal_name = ""
   age = 0
   gender = ""

   def __init__ (self, animal_name, animal_age, animal_gender):
     self.animal_name = animal_name
     self.age = int(animal_age)
     self.gender = animal_gender

   def change_name(self,str_in):
     self.animal_name = str_in

   def change_age(self,int_in):
      self.age = int(int_in)

   def change_gender(self,str_in):
      self.gender = str_in 
   
   def get_age(self):
     return self.age

   def get_name(self):
     return self.animal_name
   
   def get_gender(self):
     return self.gender


Fido = animal("Fido", 6, "Male")
print(Fido.get_name() , Fido.get_age())
