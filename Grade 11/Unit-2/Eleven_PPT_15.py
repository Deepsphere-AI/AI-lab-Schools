"""""
Ex. 15

Create another function get_values which will return the values of Application as a string.
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
      return "Name:", self.app_name
    if(type == "size"):
      self.app_size = float(name)
      return "Size:", self.app_size
    if(type == "type"):
      self.app_type = name
      return "Type:", self.app_type
    return
  
  def get_values(self):
    return "Name: " + self.app_name + " Size (GB): " + str(self.app_size) + " Type: " + self.app_type
  