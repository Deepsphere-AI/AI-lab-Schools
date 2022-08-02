"""
Ex 24.

Convert each number in the list from a int to a string
Program description: The objective of this program is to change the data type of the items in the list from integer to strings.

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

for x in range(len(vARint_list)):
  vARint_list[x] = str(vARint_list[x])
