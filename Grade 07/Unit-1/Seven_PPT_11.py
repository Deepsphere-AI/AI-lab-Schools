"""
Ex 11.

Create a System that will check whether or not a user's credentials match the correct username and password. Using user input,
if the User's username matches "Billy" and the Users password matches "Clark123", then print("Access Granted"). Otherwise, print("Access Denied").

Program description: to check if the input information matches output information for which we will be inputting information 
from user regarding the username and password . For this the general syntax is input=print(“message”) and by using the conditional 
statement if else we will check that the username obtained is equal to Billy and password = clark123 if it is then the statement under
the if statement is print, if not then the control of the loop moves to else statement the message of else statement is printed.
"""


vAR_username = input("Enter username:")
vAR_password = input("Enter password:")

print() #This is just so there is a space
if(vAR_username == "Billy" and vAR_password == "Clark123"):
  print("Access Granted")
else:
  print("Access Denied")
