"""
Ex 41.

Given a list of integer numbers, return the amount of numbers in that list that are even.

Program description: The objective of this program is to try and solve logical problems using code. 
This code specifically returns the amount of numbers in a given list that are even.


Hint: Use a loop and think about the conditions under which a number is even.

"""

vAR_numbers = [1,2,3,4,5,6,7,8] # can be any list, this is just an example
def count_evens(vAR_numbers):
  count = 0
  for vAR_x in numbers:
    if vAR_x % 2 == 0:
      count+=1
  return count
