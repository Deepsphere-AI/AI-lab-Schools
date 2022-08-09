"""
Ex 14.

Given a list of numbers, if anywhere in the list, there are 2 consecutive numbers (list[x] == list[x+1]), return true, else return false.

Program description: def is the keyword for defining a function.
The function name is followed by parameters in (). 
The colon signals the start of the function body, which is marked by indentation. 
Inside the function body, the return statement determines the value to be returned. 
Numbers is a list defining a function
"""
vAR_numbers = [12,145,14,122,142,2,3154,132,132,242,1245,235,123] # can be any list, this is just an example
def vAR_consecutive(vAR_numbers):
  for vAR_x in range(len(vAR_numbers)-1):
    if(vAR_numbers[vAR_x] == vAR_numbers[vAR_x+1]):
      return True
  return False

print(vAR_consecutive(vAR_numbers))
