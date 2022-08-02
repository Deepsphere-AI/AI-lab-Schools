"""
Ex 20.

Create a function that will take in 2 integer lists and output a list that multiplies the numbers in each list with each other.
Assume the lists are the same length.

Program description: The objective of this program is to create a function that will take in 2 integer lists 
that are of same length and multiply the numbers in each list with each other. 
For example: The first integer in the first list is 1 and the first integer in the second list is 2 then this 
program will multiply both 1 and 2 and give the answer. The same is applicable for all the items in the list.

"""

vAR_check1 = [1,2,3,4,5,6,7,8,9,10]
vAR_check2 = [1,2,3,4,5,6,7,8,9,10]

def multiply_lists(l1, l2):
  vAR_output = []
  for vAR_x in range(len(l1)):
    vAR_output.append(l1[vAR_x]*l2[vAR_x])
  return vAR_output

print(multiply_lists(vAR_check1,vAR_check2))
