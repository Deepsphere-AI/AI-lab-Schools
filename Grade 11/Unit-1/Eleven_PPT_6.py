""""
Ex. 6

Create a function that will pass in 2 strings and will output the second string inserted halfway in the first. Example: insert("Apple", "Orange") = "ApOrangeple"
"""

str1 = "Hello"
str2 = "World"

def insert(str1, str2):
  return str1[:int(len(str1)/2)] + str2 + str1[int(len(str1)/2):]

print(insert(str1,str2))