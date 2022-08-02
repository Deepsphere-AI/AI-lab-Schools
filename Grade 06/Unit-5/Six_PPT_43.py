"""
Ex 43.

Given a list of numbers, if anywhere in the list, there are 2 consecutive numbers (list[x] == list[x+1]), return true, else return false.

Program description: The objective of this program is to try and solve logical problems using code.
The code specifically returns true if there are 2 consecutive numbers in a list that are the same.
If not, it returns false.


Hint: Use the == sign to check the Boolean statement

"""
vAR_numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def vAR_consecutive(vAR_numbers):
  for vAR_x in range(len(vAR_numbers)-1):
    if(vAR_numbers[vAR_x] == vAR_numbers[vAR_x+1]):
      return True
  return False

print(vAR_consecutive(vAR_numbers))
