"""
Ex 47.

The objective of this program is to create a get function under the movie_theatre class that returns all the details about each movie in the movie_list.
"""

import random

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
  
  def details(self):
    out = "Title: " + self.title + " Runtime: " + str(self.runtime) + " Rating: " + str(self.rating) + " Year: " + str(self.year)
    return out

class movie_theatre:
  movie_list = []

  def __init__(self):
    return
  
  def random_movie(self,x):
    for i in range(x):
      rt = random.randint(120,240)
      rat = random.uniform(0,10)
      y = random.randint(1950,2021)
      self.movie_list.append(movie("",rt,rat,y))
  
  def get_movies(self):
    out = ""
    for x in self.movie_list:
      out = out + x.details() + '\n'
    return out

m1 = movie_theatre()
m1.random_movie(20)
print(m1.get_movies())
