"""
Ex 18.

Using the list created in ex. 14, given a new list, new_fruits = ["Pineapple", "Coconut", "Watermelon"], combine the two.
Program description: The objective of this program is to create a new list in the name of “new_fruits” and combine this new list with list” fruits”. 
The new_fruits (New list) consists of three values “Pineapple”, “Coconut”, “Watermelon”. A list can also have another list as an item. 
This new_fruits are then combined with the list vAR_fruits. So now the value present in the new_fruits list are now the values of fruits as well.
This program highlights the usage of append in python.

"""

vAR_fruits = ["Bannana", "Apple", "Peach"]
new_fruits = ["Pineapple", "Coconut", "Watermelon"]
for x in new_fruits:
  vAR_fruits.append(x)
