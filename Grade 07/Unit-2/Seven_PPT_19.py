"""
Ex 19.

Create a function that will take in a Boolean and 2 integers. If the boolean is True, multiply them, if the Boolean is false, divide them.

Program description:  The objective of this program is to create a program that will take in a Boolean and two integers.
If the Boolean is True, multiply them, if the Boolean is false divide those integers.
If the Boolean is true and the integers are 6 and 3 this program will multiply them and give the output as 6 *3= 18.
If the Boolean is False and the integers are 6 and 3 this program will divide them and give the output as 6/3= 2.0.

"""

def Boolean_and_2_ints(vAR_Bool, vAR_int1, vAR_int2):
  if(vAR_Bool):
    return vAR_int1*vAR_int2
  else:
    return vAR_int1/vAR_int2

print(Boolean_and_2_ints(False,6,3))
