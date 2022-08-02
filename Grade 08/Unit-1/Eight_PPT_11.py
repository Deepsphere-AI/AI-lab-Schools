"""
Ex 11.

Given a list of integer numbers, return the amount of numbers in that list that are even.

Program Description: The objective of this program is to create a function that returns the amount of even numbers present in the integer list inputted by the user.

"""

numbers = [1,2,3,4,5,6,7,8] # can be any list, this is just an example
def count_evens(numbers):
  count = 0
  for x in numbers:
    if x % 2 == 0:
      count+=1
  return count
