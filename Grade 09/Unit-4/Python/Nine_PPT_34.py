"""
Ex 34.

Program Description: The objective of this program is to create a function called “pp_sq_ft” (price per square foot) which will calculate the cost of each square foot of the property given the price of the house.

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
  
  def yard_area(self):
    return self.sq_feet - 2000 - (self.bed * 130) - (self.bath * 50)
  
  def pp_sq_ft(self):
    return self.price / self.sq_feet

