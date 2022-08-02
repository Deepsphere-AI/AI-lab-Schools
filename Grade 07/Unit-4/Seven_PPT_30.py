"""
Ex 30.

Add to the previous class a constructor that will initialize animal_type and age.

Hint: use def __init__(self,...)


Program description: The objective of this is to add to the previous class a constructor that will initialize animal_type and age.
Note: A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in 
our class. Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that
the object will need when it starts.

"""
class vAR_animal:
   vAR_animal_type = ""
   vAR_age = 0

   def __init__ (self, vAR_animal, vAR_animal_age):
     self.vAR_animal_type = vAR_animal
     self.vAR_age = int(vAR_animal_age)

   def vAR_change_type(self,vAR_str_in):
     self.vAR_animal_type = vAR_str_in

   def vAR_change_age(self,vAR_int_in):
      self.age = int(vAR_int_in)
   
   def vAR_get_type(self):
     print(self.vAR_animal_type)
    
vAR_lion = vAR_animal("lion", 10)
vAR_lion.vAR_get_type()
