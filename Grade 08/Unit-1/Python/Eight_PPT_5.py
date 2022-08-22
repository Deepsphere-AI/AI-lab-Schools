"""
Ex 5.

Using the list created in ex. 4, given the list, new_fruits = ["Pineapple", "Watermelon"], replace the corresponding value of fruits, with the corresponding values of new_fruits

Program description : The objective of this program is using the list created in exercise -4 (fruits) Create another list named new_fruits which contains values Pineapple and watermelon and to replace the corresponding values of fruits with corresponding values of new_fruits.

"""

fruits = ["Bannana", "Apple", "Peach"]
new_fruits = ["Pineapple", "Watermelon"]
for x in range(len(new_fruits)):
  fruits[x] = new_fruits[x]
print(fruits)
