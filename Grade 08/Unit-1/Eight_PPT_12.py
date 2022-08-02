"""
Ex 12.

Create a function that randomly Displays a numerical 4-digit password using random.randint(range).

Program Description: The objective of this program is to create a function that randomly displays a numerical 4-digit password using random.randint(range) 
Note- For the program to work, the built-in module Random from the python libraries must be imported successfully.

"""

import random

def randompassword():
  a = random.randint(0,9)
  b = random.randint(0,9)
  c = random.randint(0,9)
  d = random.randint(0,9)
  return str(a) + str(b) + str(c) + str(d)

print(randompassword())
