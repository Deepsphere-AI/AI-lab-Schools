"""
Ex 31.

Using user input, create a basic calculator that will add or subtract 2 numbers the user passes in. If the user passes in the numbers 1 , 2 and then types in -,
then the output should be 1-2, or -1. If the user types in 3,4 and then +, the output should be 3+4, or 7.

Program description: The objective of this program is to get an input from the user of the program and perform a variety of arithmetic functions on it before returning the
final answer. 
This program imitates a 2 function calculator. Here the user can input the two numbers and their preferred arithmetic operation (addition or subtraction).
Remember: You have to include a condition for even the worst case scenario when it comes to inputs, the desired format of input may not always be followed.

"""

vAR_num1 = int(input("What is the first number:"))
vAR_num2 = int(input("What is the second number:"))
vAR_operation = input("What is the desired operation (- or +):")

print() #This is just so there is a space
if(vAR_operation == "-"):
  print(vAR_num1 - vAR_num2)
elif(vAR_operation == "+"):
  print(vAR_num1+num2)
else:
  print("Not Valid Operation Input")
