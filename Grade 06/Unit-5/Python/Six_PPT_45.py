"""
Ex 45.

Given a list of integer numbers, find the sum of all numbers that are either odd or less than 100


Program description: The objective of this program is to try and solve logical problems using code. The code specifically asks to return the sum of numbers that are either odd or less than 100. 
Hint: Try to write a Boolean statement which checks both conditions at the same time.


"""


vAR_numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def vAR_odd_orvAR_hundred(vAR_numbers):
  vAR_total=0
  for vAR_x in vAR_numbers:
    if(vAR_x%2 == 1 or vAR_x<100):
      vAR_total+=vAR_x
  return vAR_total

print(vAR_odd_orvAR_hundred(vAR_numbers))
