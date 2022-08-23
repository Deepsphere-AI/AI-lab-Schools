"""
Ex 12.

Program description: The objective of this program is to create a constructor for the class named “application” which includes variables “app_name” and “app_size” and “app_type”.
"""

class Application:
  app_name = ""
  app_size = 0.0
  app_type = ""

  def __init__(self, name, size, type):
    self.app_name = name
    self.app_type = type
    self.app_size = size
