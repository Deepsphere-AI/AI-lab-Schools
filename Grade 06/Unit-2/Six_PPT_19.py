"""
Ex 19.

Using the list created in ex. 14, given the list, new_fruits = ["Pineapple", "Watermelon"], replace the corresponding value of fruits, 
with the corresponding values of new_fruits
Program description: The objective of this program is to replace the corresponding value of the variable fruits, 
with the corresponding value of the variable new_fruit. The len () function for getting the length of a list.

"""

vAR_fruits = ["Bannana", "Apple", "Peach"]
new_fruits = ["Pineapple", "Watermelon"]
for vAR_x in range(len(new_fruits)):
  vAR_fruits[vAR_x] = new_fruits[vAR_x]
print(vAR_fruits)
