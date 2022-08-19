"""
Ex 36.

Create a function similar to the previous that takes in a number and prints out the sum of all the numbers under it including the number itself. 
For example, sum_under(6) would print out 21.

Program description: The objective of this program is to create a user-defined function that is similar to the one before, but instead prints out 
the sum of the numbers less than the given number. 
Try it out: What do you think will be the output when the number 1 is passed under this function. (Hint: try to be careful of the range)


"""

def sum_under(num1):
  out = 0
  for x in range(num1+1):
    out+=x
  print(out)
