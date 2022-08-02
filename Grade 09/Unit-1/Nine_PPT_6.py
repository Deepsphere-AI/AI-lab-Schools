"""
Ex 6.

Program description: The objective of this program is to create a function which finds a day as the values of variables “year” , “month” and “day”. In this code we use the starting point 1/1/2021 which is a friday. In this code we assume a year to be 360 days where each month as 30 days.
"""

days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wensday", "Thursday"]
year = 2021
month = 7
day = 7

def next(self):
  if(day<31):
    day+=1
  else:
    day = 0
    month+=1
  if(month == 12):
    month = 1
    year+=1
  
def find_day(day, month, year):
  total = (day-1) + (month-1)*30 + (360 * (year-2021))
  return days[total%7]
