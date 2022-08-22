"""
Ex 3.

Write a loop to print out counting numbers from 0 - 9, but use ```while``` instead of for

Program description : The objective of this program is to print the numbers in range using a while loop. Here we declare a variable “x” and initialize it as 0 and give it with a while condition that the value should be lesser than 10.and we also increment which is increasing the value of x by 1, each time the loop runs. And we print so each time the loop runs it will increase its value by 1 and check with the condition and if the condition satisfies its proceeds or if not, the loop terminates.
Note: The value can also decrement by using the condition “x=x-1”. But for decrementing we have to initialize the value of x as 10.
Try it out : Try printing 0-9 using a while loop by decrementing. 

"""

x = 0
while x < 10:
  print(x)
  x = x+1    
  
  #Or x+=1 also works
