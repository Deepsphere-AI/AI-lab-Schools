"""
Ex 9.

Now create the variable out_list at the top and the function decrypt which will decrypt all the values with their corresponding keys and append their values to the out list.
"""

class Decryptor:
  key_list = []
  Encryptor_list = []
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  out_list = []

  def __init__(self):
    return
  
  def add_encryptor(self, in_string, key):
    self.key_list.append(key)
    self.Encryptor_list.append(in_string)
  
  def decrypt(self):
    self.letters.reverse()
    for x in range(len(self.key_list)):
      out = ""
      en_str = self.Encryptor_list[x]
      for i in range(len(en_str)):
        for y in range(len(self.letters)):
          if(self.letters[y] == en_str[i]):
            temp = y
            temp = temp + self.key_list[x]
            temp = temp%26
            out = out + self.letters[temp]
      self.out_list.append(out)


  

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
  
  def get_values(self):
    return "Input String: " + self.in_string + ", Output String: " + self.out_string + ", Key: " + str(self.key) 

e1 = Encryptor("Hello", 30)
e1.change_key(1)
e1.change_string("Apple")
e1.encrypt()
print(e1.get_values())

d1 = Decryptor()
d1.add_encryptor("bqqmf", 1)
d1.add_encryptor("ifmmp", 1)
d1.decrypt()