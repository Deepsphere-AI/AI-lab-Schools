"""
Ex 13.

Program Description: The objective of this program is to create a function that can print the sum of all integers that are odd or less than 100.
"""

numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def odd_or_hundred(vAR_numbers):
  vAR_total=0
  for vAR_x in vAR_numbers:
    if(vAR_x%2 == 1 or vAR_x<100):
      vAR_total+=vAR_x
  return vAR_total

print(odd_or_hundred(numbers))
