"""
Ex 22.

Create a constructor for the class which takes in a passed in word and sets the self word equal to that.
"""

class Word:
  word = ""
  letter_count = []
  letters = []

  def __init__(self, s1):
    self.word = s1