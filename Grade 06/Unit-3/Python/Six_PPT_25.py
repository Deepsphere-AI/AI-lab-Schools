"""
Ex 25.

Finally, Add all the values to make 1 long string with each number seperated by a space

Program description: The objective of this program is to add all the values of a list containing different strings and make a large string.
"""

vARint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(len(vARint_list)):
  vARint_list[x]*=12

vAR_add = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for vAR_x in range(len(vARint_list)):
  vARint_list[x] = (vARint_list[x] + vAR_add[x])

vAR_total = 0
for x in range (len(vARint_list)):
  vAR_total+= vARint_list[x]

for x in range(len(vARint_list)):
  vARint_list[x] = str(vARint_list[x])

print_me = ""
for x in range(len(vARint_list)):
  print_me = print_me + " " + vARint_list[x]
print(print_me)
