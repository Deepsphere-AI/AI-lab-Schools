"""
Ex 17.

Create a function that will combine a list of strings and ouput a sentence of the strings in the list. Example: if list = ["This", "is", "a", "test"], 
then the output would be "This is a test"

Program description: Program description: The objective of this program is to create a function that combines a list of strings in the list. 
For example: List = [“This ”, “ is ”, “ a ”,” test ”,] = This is a test

Note: Each string in the list would be equal to each word in the sentence.

"""

vAR_check = ["This", "is", "a", "test"]
def vAR_sentence(vAR_check):
  vAR_output = ""
  for vAR_x in vAR_check:
    vAR_output = vAR_output + vAR_x + " "
  return vAR_output

print(vAR_sentence(vAR_check))
