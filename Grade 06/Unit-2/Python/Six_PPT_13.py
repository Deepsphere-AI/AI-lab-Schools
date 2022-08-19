"""
Ex 13.

Write a loop to print out counting numbers from 0 - 9, but use while instead of for\

Program description: The objective of this program is to print numbers from 0 – 9 using a while loop. 
The variable vAR_x equals 0, While variable vAR_x < 10 it prints the value in variable vAR_x. This program keeps repeating till vAR_x reaches 9.
Since the starting value of vAR_x is 0 it will start from 0 and end in 9.
Note: While loop in python is used to execute a block of statement repeatedly until a given condition is satisfied.

"""

vAR_x = 0
while vAR_x < 10:
  print(vAR_x)
  vAR_x = vAR_x+1    
  #Or vAR_x+=1 also works
