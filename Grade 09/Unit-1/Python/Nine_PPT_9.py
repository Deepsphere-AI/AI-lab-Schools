"""
Ex 9.

Program description: The objective of this program is to create a function named “next_month” which calculates how many days are left until the next month.
The simple calculation in this code is “30-current date/day” .

Note: This program highlights the usage of return function in python.

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

def next_month():
  return 30-day
