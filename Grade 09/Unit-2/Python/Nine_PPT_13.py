"""
Ex 13.

Program Description: The objective of this program is to create a function that will take in two strings. One string will be determining what feature will be changed and the other will be the value that will be updated.

Example: update(“13”, “size”) will change the size to 13.

"""

class Application:
  app_name = ""
  app_size = 0.0
  app_type = ""

  def __init__(self, name, size, type):
    self.app_name = name
    self.app_type = type
    self.app_size = size
  
  def update(self, name, type):
    if(type == "name"):
      self.app_name = name
    if(type == "size"):
      self.app_size = float(name)
    if(type == "type"):
      self.app_type = app_name
