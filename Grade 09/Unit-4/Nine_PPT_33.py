"""
Ex 33.

Program Description: The objective of this program is to create a function called “yard_area()” which will return the remaining square footage of the property that is the yard. 

Note: Each bedroom requires a minimum of 130 square feet and each bathroom requires a minimum of 50 square feet. Assume that there are 2000 square feet in the house that are not a part of the bed or bathrooms.

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

