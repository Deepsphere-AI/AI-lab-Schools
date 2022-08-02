"""
Ex 15.

Given a list of integer numbers, find the range of the list (the maximum - minimum value)

Program description: defining a function range min and max of numbers is 0 if x is lesser than min then print minx
"""


vAR_numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def range(vAR_numbers):
  vAR_min = vAR_numbers[0]
  vAR_max = vAR_numbers[0] 
  for vAR_x in vAR_numbers:
    if(vAR_x < vAR_min):
      vAR_min = vAR_x
    if(vAR_x > vAR_max):
      vAR_max = vAR_x
  return vAR_max-vAR_min

print(range(vAR_numbers))
