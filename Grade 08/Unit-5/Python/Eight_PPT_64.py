"""
Ex 45.

The objective of this program is to create a ‘random movie’ which creates a specified number of movies with a random runtime, random rating, and random year with a blank title. 
Note: Remember to import the random module at the start of your code.

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

m1 = movie_theatre()
m1.random_movie(20)
