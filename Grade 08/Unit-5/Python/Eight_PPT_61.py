"""
Ex 42.

The objective of this program is create a constructor for the movie class.

"""

class movie:
  title = ""
  runtime = 0
  rating = 0.0
  year = 0

  def __init__(self, title, runtime, rating, year):
    self.title = title
    self.rating = rating
    self.runtime = runtime
    self.year = year

m1 = movie("Titanic", 210, 7.8, 1997)
