"""
Ex 26.

Create a class text which will have the variable word_list.
"""

class Text:
  word_list = []

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
