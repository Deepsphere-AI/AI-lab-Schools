""""

Ex. 5

Create a function that will check whether the sum of a list that is passed in equal to 21

"""

check = [1,2,-3,3,3,4,5,6,2,-2]
def sum21(list):
  total = 0
  for x in check:
    total+=x
  if(total == 21):
    return True
  else:
    return False

print(sum21(check))