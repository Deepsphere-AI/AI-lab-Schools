"""
Ex 38.

Create a function that scrambles the order of a sentence inputted by a user. The last and first word will be switched and the second word will be deleted. Use a switching algorithm in order to swich the first and last words. This excersise is more difficult then the previous one, but try your best!

Hint: Using the method .split(" ") on a string will split the sentence into a list where each word occupies a slot.


Program description: The objective of this program is to create a function which performs several tasks altogether.
This code specifically creates a function that scrambles the order of a  sentence given by the user.
The last and first word will be switched and the second word will be deleted. 
It uses a ‘Switching algorithm’ (using a temp variable) to do the same.
This is a little more difficult compared to the rest.
Hint: Using the method.split(" ") on a string will split the sentence into a list where each word occupies a slot.

"""


def sentence_scrambler(sent):
  words = sent.split(" ")
  output = ""
  #Below is a common switching algorithm
  temp = words[0] #Temporarily stores value that will be replaced
  words[0] = words[len(words)-1] # Replaces value 1 with value 2
  words[len(words)-1] = temp # Replace value 2 with temp which stores value 1
  words[1] = ""
  for x in words:
    output = output + x + " "
  print(output)
sentence_scrambler("The last and first word")
