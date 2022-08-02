"""
Ex 21.

Create a function that will take in a string and output the string but with each character doubled. For example: double("Apple") = "AAppppllee"

Program description: The objective of this program is to create a function that will take output the string but with each character doubled.
For example:
                    *(“Apple”) = AAppppllee
                    *(“Pear”) = PPeeaarr
Note : The each letter is doubled

"""

vAR_str1 = "Apple"

def double(vAR_string):
  vAR_output = ""
  for vAR_x in range(len(vAR_string)):
    vAR_output = vAR_output + vAR_string[vAR_x] + vAR_string[vAR_x]
  return vAR_output

print(double(vAR_str1))
