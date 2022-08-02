"""
Ex 28.

Grab 2 numbers through user input and print out the result when they are multiplied

Hint: Use int() to convert string to an int.

Program description: The objective of this program is to get an input from the user of the program and perform functions on it before printing it out.
This program specifically asks for 2 numbers and multiplies them before printing it out.
Remember: The input function always takes user input as it is and converts it into a String.
To perform arithmetic operations like multiplication, you must first convert it into an Integer data type using the int keyword.

"""

vAR_num1 = int(input("Enter a number:"))
vAR_num2 = int(input("Enter another number:"))

print() #This is just so there is a space
print(vAR_num1 * vAR_num2)
