"""
Ex 18.

Create a function that will take in a list of random numbers. Output those numbers, but sortest from least to greatest.

Program description: The objective of this program is to arrange a random set of numbers in ascending order (shortest to greatest).
In this program the list contains a random set of numbers such as [6,5,3,7,9,2,8,1,4,10]. But the output of this program will be [1,2,3,4,5,6,7,8,9,10].
Note: This program works for any set of natural numbers.

"""

vAR_check = [6,5,3,7,9,2,8,1,4,10]
def vAR_sort(vAR_check):
  vAR_out_list = vAR_check
  for vAR_x in range(len(vAR_out_list)):
    for vAR_x in range(len(vAR_out_list)-1):
      if(vAR_out_list[vAR_x] > vAR_out_list[vAR_x+1]):
        vAR_temp = vAR_out_list[vAR_x]
        vAR_out_list[vAR_x] = vAR_out_list[vAR_x+1]
        vAR_out_list[vAR_x+1] = vAR_temp
  return vAR_out_list

print(vAR_sort(vAR_check))
