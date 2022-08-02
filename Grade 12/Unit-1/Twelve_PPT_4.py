""""

Ex. 4

Create the function pp_sq_ft or price per square foot, which will calculate how much each sq_foot of the property costs based on the price of the house.

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

