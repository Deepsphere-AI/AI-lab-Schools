"""
Ex 7.

Say an apple costs .59 cents and a pear costs .99 cents. Using user input and ommiting any taxes, find out how much it costs if one buys 3 apples and 4 pears.

Program description : The objective of this program is to find out how much it costs if one buys 3 apples and 4 pears. If one apple costs 0.59 cents and one pear costs 0.99 cents. It will calculate the total amount.

"""

apples  = int(input("How many apples:"))
pears = int(input("How many pears:"))

print() #This is just so there is a space
print(apples * .59 + pears * .99)
