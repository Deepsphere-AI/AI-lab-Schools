"""
Ex 46.

Create a function that randomly Displays a numerical 4-digit password using random.randint(range). Remeber to type import random at the top!

Program description: The objective of this program is to try and solve logical problems using code. 
The code specifically asks to return a randomly generate 4 digit numeric password. You will learn to work with the randint() function. 
Hint: Remember to type import random to import the random module at the beginning.
Or else, you won't be able to use the randint() function.
Remember: The random module is a built-in module to generate the pseudo-random variables.
It can be used to perform some action randomly such as to get a random number, selecting a random element from a list, shuffle elements randomly, etc.

"""
import random

def randompassword():
  vAR_a = random.randint(0,9)
  vAR_b = random.randint(0,9)
  vAR_c = random.randint(0,9)
  vAR_d = random.randint(0,9)
  return str(vAR_a) + str(vAR_b) + str(vAR_c) + str(vAR_d)

print(randompassword())
