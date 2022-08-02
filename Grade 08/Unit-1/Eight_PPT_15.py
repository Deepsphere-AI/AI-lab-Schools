"""
Ex 15.

Program Description: The objective of this program is to create a function that will pass in 2 strings and output the second string inserted halfway in the first. Ex- Insert(“Apple”, “Orange”) = “ApOrangeple”

Note- Do not forget to add (“  ”) for the strings

"""

vAR_str1 = "Apple"
vAR_str2 = "Orange"

def insert(vAR_str1, vAR_str2):
  return vAR_str1[:int(len(vAR_str1)/2)] + vAR_str2 + vAR_str1[int(len(vAR_str1)/2):]

print(insert(vAR_str1,vAR_str2))
