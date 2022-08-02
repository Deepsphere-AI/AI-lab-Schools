"""
Ex 29.

Say an apple costs .59 cents and a pear costs .99 cents. Using user input and ommiting any taxes, find out how much it costs if one buys 3 apples and 4 pears.

Program description: The objective of this program is to get an input from the user of the program and perform functions on it before printing it out.
This program specifically calculates the total cost of apples and pears at the rate of .59 cents per apple and .99 cents per pear.
It inputs the individual number of apples and pears before finding the total cost.
Try it out: Try to find the cost of 3 apples and 4 pears, then try finding the cost of 8 apples and 12 pears.

"""
vAR_apples  = int(input("How many apples:"))
vAR_pears = int(input("How many pears:"))

print() #This is just so there is a space
print(vAR_apples * .59 + vAR_pears * .99)
