"""
Exercises 11 - 25 have been about loops and lists, both key concepts in coding. This review is to check your understanding on the topics.

Prompt: Given a list of conditionals (True or False), Count how many times True occurs and how many times False occurs. Then, set all values of the list to True if True occurs more, or False if False occurs more. If True and False are equal, set the first half to True, and Second half to false.

Conditonal_List = [True, False, True, True, False, False, True, True, True, True, False, False, True, False, False, False, True, True, False, False]
"""

Conditonal_List = [ True, False, True, True, False, False, True, True, True, True, False, False, True, False, False, False, True, True, False, False]
True_count = 0;
False_count = 0;

for x in range(len(Conditonal_List)):
  if(Conditonal_List[x] == True):
    True_count+=1
  else:
    False_count+=1
if(True_count > False_count):
  for x in range(len(Conditonal_List)):
    Conditonal_List[x] = True
elif (True_count < False_count):
  for x in range(len(Conditonal_List)):
    Conditonal_List[x] = False
else:
  for x in range(len(Conditonal_List)//2):
    Conditonal_List[x] = True
  for x in range(len(Conditonal_List)//2,len(Conditonal_List)):
    Conditonal_List[x] = False
print(Conditonal_List)