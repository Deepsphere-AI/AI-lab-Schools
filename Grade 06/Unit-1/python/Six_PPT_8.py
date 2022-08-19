"""
Ex 8.

Print whether a number is even or odd
Hint: Use %

Program description: The objective of this program is to print whether a number is odd or even. This program highlights the function of if statement and else statement. 
Then this program will print even or else odd. Any number positive or negative which is divisible by 2 are declared to be even numbers which aren’t are declared to be odd numbers. 
This program reads an input integer using input (). When this input is divided by 2 and leaves a remainder other than 0 it is printed as odd number. 
When input is = 0 it is printed as even number.

"""

vARinput_num = 141
if(vARinput_num%2 == 0):
  print("even")
else:
  print("odd")
