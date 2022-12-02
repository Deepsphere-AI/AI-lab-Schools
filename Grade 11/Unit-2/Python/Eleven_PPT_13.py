"""""
Ex. 13

Give the application the function update which will take in 2 strings. One will determine what feature needs to be update. The other will contain the value that will update. ie update("13", "size") will change the size to 13. update("New", "name") will change the name to "New".
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