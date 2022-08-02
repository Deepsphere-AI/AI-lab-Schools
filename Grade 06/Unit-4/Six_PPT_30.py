"""
Ex 30.

Create a System that will check whether or not a user's credentials match the correct username and password. Using user input,
if the User's username matches "Billy" and the Users password matches "Clark123", then print("Access Granted"). Otherwise, print("Access Denied").

Program description: The objective of this program is to get an input from the user of the program and test it against an already existing condition. 
This program specifically gets an input of username and password and decides whether it matches the already set username and password.
Then it either grants access or denies access.
Notice: Doesn’t this program seem to simulate the log in pages of a website?


"""

vAR_username = input("Enter username:")
vAR_password = input("Enter password:")

print() #This is just so there is a space
if(vAR_username == "Billy" and vAR_password == "Clark123"):
  print("Access Granted")
else:
  print("Access Denied")
