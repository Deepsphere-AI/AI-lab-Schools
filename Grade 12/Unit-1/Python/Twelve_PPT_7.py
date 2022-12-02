""""
Ex. 7

Add to the class a constructor and a function add_houses, which will take in x and add x number of random houses to the house list. Give each house either 2, 2.5, or 3 bed/bath, a random price from 800,000 to 1,200,000, and a random square feet from 4,000 to 6,000.
"""

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

class residential_area:
  house_list = []
  avg_price = 0.0
  avg_sq_feet = 0.0

  def __init__(self):
    return
  
  def rand_house(self,x):
    bed = random.randint(4,6)/2
    bath = random.randint(4,6)/2
    for i in range(x):
      self.house_list.append(house(bed,bath,random.randrange(800000,1200000),random.randrange(4000,6000)))

r1 = residential_area()
r1.rand_house(40)
  
