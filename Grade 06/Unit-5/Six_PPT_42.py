"""
Ex 42.

Given a list of integer numbers, return the average value of the numbers

Program description: The objective of this program is to try and solve logical problems using code.
This code specifically returns the average of numbers in a given list.

Hint: Try to use the len() function to get the number of elements in the list.

"""

vAR_numbers = [10,12,13,14,12,11,15,19,7,6,46] # can be any list, this is just an example
def vAR_average(vAR_numbers):
  vAR_total = 0
  for vAR_x in vAR_numbers:
    vAR_total+=vAR_x
  return vAR_total/len(vAR_numbers)

print(vAR_average(vAR_numbers))
