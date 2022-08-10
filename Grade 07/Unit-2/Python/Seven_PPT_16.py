"""
Ex 16.

Create a function that will check whether the sum of a list that is passed in equal to 21
"""

vAR_check = [1,2,-3,3,3,4,5,6,2,-2]
def vAR_sum21(list):
  vAR_total = 0
  for vAR_x in vAR_check:
    vAR_total+=vAR_x
  if(vAR_total == 21):
    return True
  else:
    return False

print(vAR_sum21(vAR_check))
