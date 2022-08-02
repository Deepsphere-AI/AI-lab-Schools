"""
Ex 10.

Given a list of integer numbers, find the range of the list (the maximum - minimum value)

Program Description: The objective of this program is to create a function that can print the range(Maximum- minimum list) of integers inputted by the user.
Note- Range is the difference between the highest and lowest values

"""

numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def range(numbers):
  min = numbers[0]
  max = numbers[0] 
  for x in numbers:
    if(x < min):
      min = x
    if(x > max):
      max = x
  return max-min

print(range(numbers))
