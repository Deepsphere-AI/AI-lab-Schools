"""
Ex 23.

Create a function to_letters which splits a string into uniqe letters, meaning that "Hello" gets split into H, e, l, and o. Set the letters list to contain each of these letters.
"""

class Word:
  word = ""
  letter_count = []
  letters = []

  def __init__(self, s1):
    self.word = s1
  
  def to_letters(self):
    self.letters.append(self.word[0])
    for x in range(len(self.word)):
      temp = True
      for i in range(len(self.letters)):
        if(self.word[x] == self.letters[i]):
          temp = False
          break
      if temp:
        self.letters.append(self.word[x])
    return self.letters

w1 = Word("Mississippi")
print(w1.to_letters())

