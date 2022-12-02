""""

Ex. 3

Each bedroom requires at least 130 sq_feet and each bathroom requres at least 50 sq_feet. Assuming that there are 2000 sq feet in the house itself not part of the bed or bathrooms, create the function yard_area() that will return the remaining sq_feet of the property that is the yard area.
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

