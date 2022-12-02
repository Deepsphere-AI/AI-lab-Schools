""""

Ex. 3

Grab the username and password through user input and return the result. Make sure this is inside a function.

"""

def get_credentials():
  username = input("Enter username:")
  password = input("Enter password:")

  return("Username: " + str(username) + " Password: " + str(password))

get_credentials()