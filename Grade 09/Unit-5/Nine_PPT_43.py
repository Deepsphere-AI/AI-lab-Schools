"""
Ex 43.

The objective of this program is to create another class called movie_theatre which will contain a list of movie class objects.
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

class movie_theatre:
  movie_list = []
