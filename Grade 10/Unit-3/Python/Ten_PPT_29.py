"""
Ex 29.

Create a function count_letters which similar to the previous word class, will count and print how many different letters there are across the entire text.
"""

import random

class Text:
  word_list = []
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
  letter_count = []
  words = 0

  def __init__(self,x):
    self.words = x
  
  def random(self):
    for x in range(self.words):
      temp = ""
      for x in range(5):
        temp = temp + self.letters[random.randint(0,25)]
      self.word_list.append(temp)
    return self.word_list
  
  def count_letters(self):
    for x in range(26):
      self.letter_count.append(0)
    for x in self.word_list:
      for j in range(len(x)):
        for i in range(len(self.letters)):
          if(x[j] == self.letters[i]):
            self.letter_count[i]+=1
    for x in range(len(self.letters)):
      print(self.letters[x] + " : " + str(self.letter_count[x]))


class Word:
  word = ""
  letter_count = []
  letters = []

  def __init__(self, s1):
    self.word = s1
    self.to_letters()
    self.count_letters()
  
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
  
  def count_letters(self):
    for x in self.letters:
      temp = 0
      for i in range(len(self.word)):
        if x == self.word[i]:
          temp+=1
      self.letter_count.append(temp)
    return self.letter_count


w1 = Word("Mississippi")
print(w1.to_letters())
print(w1.count_letters())

t1 = Text(10)
print(t1.random())
t1.count_letters()
