""""
Ex. 6

Create the class residential_area which has the list house_list, avg_price,and avg_sq_feet.
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

class residential_area:
  house_list = []
  avg_price = 0.0
  avg_sq_feet = 0.0
  