"""
Ex 12.

Create a function that takes in a number and prints out the sum of all the numbers under it including the number itself. For example, sum_under(6) = 21

Program description: def is the keyword for defining a function. The function name is followed by parameters in ().
The colon signals the start of the function body, which is marked by indentation.
Inside the function body, the return statement determines the value to be returned. 
Here variable out is initialized to 0 and num 1 variable is incremented by 1 so this keep printing the sum of numbers by running the loop. 
"""
def sum_under(vAR_num1):
  vAR_out = 0
  for vAR_x in range(vAR_num1+1):
    vAR_out+=vAR_x
  print(vAR_out)
  
sum_under(6)
