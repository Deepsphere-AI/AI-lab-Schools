"""
Ex 44.

Given a list of integer numbers, find the range of the list (the maximum - minimum value)

Program description: The objective of this program is to try and solve logical problems using code.
The code specifically asks to return the range of a given list of numbers.
You first have to try and get the maximum value, then the minimum value and then find and return the range.


Hint: Range = Max value – Min value

"""

vAR_numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def range(vAR_numbers):
  min = vAR_numbers[0]
  max = vAR_numbers[0] 
  for vAR_x in vAR_numbers:
    if(vAR_x < min):
      min = vAR_x
    if(vAR_x > max):
      max = vAR_x
  return max-min

print(range(vAR_numbers))
