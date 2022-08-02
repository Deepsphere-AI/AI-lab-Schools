"""
Ex 23.

Add Up all the values from each cell in the vARint_list (From Ex 22)
Program description: The objective of this program is to add up all the value from each call in the vARint_list.

"""

vARint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(len(vARint_list)):
  vARint_list[x]*=12

vAR_add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for x in range(len(vARint_list)):
  vARint_list[x] = (vARint_list[x] + vAR_add[x])

vAR_total = 0
for x in range (len(vARint_list)):
  vAR_total+= vARint_list[x]
