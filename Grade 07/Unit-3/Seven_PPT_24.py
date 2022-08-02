"""
Ex 24.

Create a function that will pass in a string that is a sentence, and output a list with each item in the list containg a word from the sentence. 
Example: toList("Convert this to a list") = ["Convert", "this", "to", "a", "list"]

Hint: Use .split(" ")

Program description: The objective of this program is to convert a string that is a sentence to a list. In Ex.17 we have seen how to convert a list into a sentence.
This program is the exact opposite of that. Here we convert a sentence into a list.
For example: -
                  Hello, everyone how are you = [“Hello”, everyone”,“how”, “are”, “you”]
                  Convert this to a list = [“Convert”, “this”, “to”, “a”, “list”]

"""

vAR_str = "Convert this to a list"

def toList(vAR_string):
  return vAR_string.split(" ")

print(toList(vAR_str))
