"""
Ex 4.

Create the functions change_string and change_key which will change their corresponding attributes.
"""

class Encryptor:
  in_string = ""
  out_string = ""
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  key = 0

  def __init__(self, in_str, in_key):
    self.key = in_key
    self.in_string = in_str

  def encrypt(self):
    self.in_string = self.in_string.lower()
    for x in range(len(self.in_string)):
      for i in range(len(self.letters)):
        if(self.letters[i] ==  self.in_string[x]):
          temp = i + self.key
          temp = temp%26
          self.out_string = self.out_string + self.letters[temp]
    return self.out_string
  
  def change_string(self, in_str):
    self.in_string = in_str
  
  def change_key(self, key):
    self.key = key
  
e1 = Encryptor("Hello", 30)
e1.change_key(1)
e1.change_string("Apple")
print(e1.encrypt())