"""
Ex 37.

Create 2 functions where one multiplies by 5 and one takes the output of the first one and adds 4 to the output of it.

Program description: The objective of this program is to create 2 user-defined functions.
The function call of one function is placed within the other function.
The first function ‘vAR_times5’ multiplies a given number by 5 and then returns it. 
The second function calls ‘vAR_times5’ and then adds 4. 
Remember: A function can return data as a result. 
If there is no value that is returned by a function, it is called a void function.

"""
def vAR_times5(vAR_num1):
  return vAR_num1*5

def vAR_plus4(vAR_num1):
  return vAR_times5(vAR_num1)+4
