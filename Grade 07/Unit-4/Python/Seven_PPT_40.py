"""
Ex 40.

Using the code for the last excersise, change Sally's age to 6 and compare it with the age of Gumpy. If it is equal print True, otherwise print False.

Program description: The objective of this function is to perform actions on the 2 objects Fido and Sally (created in 36 and 39). 
We first change the age attribute of Sally from 15 to 6. 
Then, we use a Boolean statement to check if the age attribute of the 2 objects are the same.
Note: If the Boolean was before the code to change age attribute of Sally, then the answer will be different.

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
Fido.change_name("Gumpy")

Sally = animal("Sally", 15, "Female")
Sally.change_age(6)

print(Fido.get_age() == Sally.get_age())
