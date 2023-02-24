"""
Ex 49.

The objective of this program is to create a function sort_rating that will sort the movie_list by rating, least to greatest. Use for loops and conditional statements to do the same. 
Note: Make sure to use the correct format while accessing the members of the list.

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
  
  def get_rating(self):
    return self.rating

class movie_theatre:
  movie_list = []

  def __init__(self):
    return
  
  def random_movie(self,x):
    for i in range(x):
      rt = random.randint(120,240)
      rat = random.uniform(0,10)
      y = random.randint(1950,2021)
      self.movie_list.append(movie("",rt,round(rat,1),y))
  
  def get_movies(self):
    out = ""
    for x in self.movie_list:
      out = out + x.details() + '\n'
    return out
  
  def sort_rating(self):
    for i in range(len(self.movie_list)):
      for x in range(len(self.movie_list) - 1):
        if(self.movie_list[x].get_rating() > self.movie_list[x+1].get_rating()):
          temp = self.movie_list[x+1]
          self.movie_list[x+1] = self.movie_list[x]
          self.movie_list[x] = temp

m1 = movie_theatre()
m1.random_movie(20)
m1.sort_rating()
print(m1.get_movies())
