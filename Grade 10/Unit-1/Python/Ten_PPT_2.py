"""
Ex 2.

Create a constructor which will take in the input string, and a key (int).
"""

class Encryptor:
  in_string = ""
  out_string = ""
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  key = 0

  def __init__(self, in_str, in_key):
    self.key = in_key
    self.in_string = in_str