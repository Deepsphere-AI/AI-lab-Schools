"""
Ex 24.

Create a function count_letters which adds how many times each letter in the string shows up corresponding to it's location in letter_count. Then append it to letters, For examples, if we use the word Hello, letter_count = ['H', 'e' , 'l', 'o'], and letters = [1, 1, 2, 1]
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
