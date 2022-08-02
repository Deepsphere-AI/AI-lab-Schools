""""
Ex. 8

Add to the class a function called get_houses that returns the bed, bath, price, and sq_feet of each house with each line corresponding each house. You will need to edit the house class also."""

import random

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
  
  def get_values(self):
    return "Bed: " + str(self.bed) + " Bath: " + str(self.bath) + " Price: " + str(self.price) + " Square Feet: " + str(self.sq_feet)

class residential_area:
  house_list = []
  avg_price = 0.0
  avg_sq_feet = 0.0

  def __init__(self):
    return
  
  def rand_house(self,x):
    for i in range(x):
      bed = float(random.randint(4,6))/2
      bath = float(random.randint(4,6))/2
      self.house_list.append(house(bed,bath,random.randrange(800000,1200000),random.randrange(4000,6000)))
  
  def get_houses(self):
    out = ""
    for x in self.house_list:
      out = out + x.get_values() + '\n'
    return out

r1 = residential_area()
r1.rand_house(40)
print(r1.get_houses())