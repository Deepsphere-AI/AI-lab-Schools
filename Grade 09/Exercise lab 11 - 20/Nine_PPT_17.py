"""
Add a constructor to the Computer class
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
  
class Computer:
  comp_name = ""
  available_space = 0.0
  total_space = 0.0
  app_list = []

  def __init__(self, name, av, to, num):
    self.comp_name = name
    self.available_space = av
    self.total_space = to