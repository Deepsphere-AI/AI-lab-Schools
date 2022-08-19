"""
Ex 40.

Revisting the previous topics, create a 4 function calculator using functions that can add, subtract, multiply and divide. Take in user input like before.

Program description: The objective of this program is to create a simple user-defined function that takes in an input from the
user of the program and performs a variety of arithmetic functions on it before returning the final answer.
This program imitates a 4 function calculator. Here the user can input the two numbers and their preferred arithmetic operation(addition or subtraction).
Remember: Unless a function is called, python will not perform the code under the specific function. Hence, function calls are very important.
Try to differentiate between arguments and parameters of a function.

"""

num1 = int(input("What is the first number:"))
num2 = int(input("What is the second number:"))
operation = input("What is the desired operation (- , + , / or *):")

def add(n1, n2):
  return n1+n2

def subtract(n1, n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2
  
if(operation == "+"):
  print(add(num1,num2))
elif(operation == "-"):
  print(subtract(num1,num2))
elif(operation == "*"):
  print(multiply(num1,num2))
elif(operation == "/"):
  print(divide(num1,num2))
else:
  print("Invalid Operation")
