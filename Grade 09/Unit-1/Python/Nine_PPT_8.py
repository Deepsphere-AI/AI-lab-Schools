"""
Ex 8.

Program description: The objective of this program is to create a function named ”days” which will find out how many days until a specific date is passed in.

"""

days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wensday", "Thursday"]
year = 2021
month = 1
day = 23

def next():
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

def print_date():
  return find_day(day,month,year) + ", " + str(month) + "/" + str(day) + "/" + str(year)

def days_until(day1, month1, year1):
  return ((day1-1) + (month1-1)*30 + (360 * (year1-2021))) - ((day-1) + (month-1)*30 + (360 * (year-2021)))
