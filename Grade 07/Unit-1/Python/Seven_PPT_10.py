"""
Ex 10.

Grab 2 numbers through user input and print out the result when they are multiplied

Hint: Use int() to convert string to an int.

Program description: Program description in this program we have declared two variables num1 and num2 and we have initialized
these variables with integer data value and input function signifies accepting values from user of particular data type the 
string inside double quotes will be printed in output by default. Print function is an output statement which performs operation
in absence of quotes but print the message inside the quotes.
NOTE: INPUT IS USED TO GET THE VALUES OF PARTICULAR DATA TYPE FROM THE USER WHILR PRINT STATEMENT IS USED TO PERFORM OPERATION 
IN ABSENCE OF QUOTES AND PRINT THE MESSAGE IF INSIDE QUOTES.TO LEAVE SPACE USE PRINT ()

"""

vAR_num1 = int(input("Enter a number:"))
vAR_num2 = int(input("Enter another number:"))

print() #This is just so there is a space
print(vAR_num1 * vAR_num2)
