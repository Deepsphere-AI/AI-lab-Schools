"""
Ex 32.

Program Description: The objective of this program is to create a constructor that will take in the variables as parameters and set them equal to one another.

"""

class house:
  bed = 0.0
  bath = 0.0
  price = 0.0
  sq_feet = 0.0

  def __init__(self, bed, bath, price, sq_feet):
    self.bed = bed
    self.bath = bath
    self.price = price
    self.sq_feet = sq_feet
