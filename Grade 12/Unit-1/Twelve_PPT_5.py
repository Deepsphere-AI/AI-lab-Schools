""""

Ex. 5

Using round() in python, make sure all the price values and the sq_feet are rounded to 2 decimal places and the bed and bath is rounded to 1.
"""

class house:
  bed = 0.0
  bath = 0.0
  price = 0.0
  sq_feet = 0.0

  def __init__(self, bed, bath, price, sq_feet):
    self.bed = round(bed,1)
    self.bath = round(bath,1)
    self.price = round(price,2)
    self.sq_feet = round(sq_feet,2)
  
  def yard_area(self):
    return round((self.sq_feet - 2000 - (self.bed * 130) - (self.bath * 50)),2)
  
  def pp_sq_ft(self):
    return round((self.price / self.sq_feet),2)


