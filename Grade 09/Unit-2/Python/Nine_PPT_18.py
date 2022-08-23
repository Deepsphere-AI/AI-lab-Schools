"""
Ex 18.

Program Description: The objective of this program is to create a new function called “add_app” to the “Computer” class. This function will add an app to the app list and also update the “availabe_space” variable. 

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
  
  def get_size(self):
    return self.app_size
  
class Computer:
  comp_name = ""
  available_space = 0.0
  total_space = 0.0
  app_list = []

  def __init__(self, name, av, to):
    self.comp_name = name
    self.available_space = av
    self.total_space = to
  
  def add_app(self, app):
    self.app_list.append(app)
    self.available_space = self.available_space - app.get_size()
  
  
mycomp = Computer("My PC", 22.33, 50)
mycomp.add_app(Application("Settings", .98, "System"))
