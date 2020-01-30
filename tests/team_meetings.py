"""
It's Friday afternoon at 3:00pm. The week is coming to a close. All production
systems are green. The deployment went to plan. There are murmurs of after-work
pizza and hot wings.

But all of a sudden, there is a pattering of speedy footsteps coming your way.
It's your manager Tom. No one likes Tom. (No, Tom is actually really cool.
Everyone loves Tom.)

He comes to you with an urgent demand! "<candidate name>, we just had a major
feature request come in from our top client XYZ Corp. They need a way of
determining which dates all of their team meetings will be for the next 365
days. Without this valuable information, they cannot ensure that all
stakeholders are present so no decisions will get made and no products will be
built and no products will be sold and revenue will be made and there will be
no money to pay employees and those employees will have to give up their avocado
toast brunches!

HELPPPPP!!!
"""
import calendar
from datetime import datetime

cal = calendar.Calendar(firstweekday=0)  # Create a calendar
months = calendar.month_name[1:] # Get the names of calendar months
today = datetime.today()
meeting_days = [] # Store days of month for team meeting
year = {}

for month in range(0, 12):
        for day in cal.itermonthdates(2020, month):
                month = months[day.month-1]
                # If day is on Friday, add to meeting days
                if day.isoweekday() == 5:
                        meeting_days.append(day.day)
                        if month in year:
                                year[month].append(day.day)
                        else:
                                year[month] = [day.day]

for x, month_number in zip(months, year.keys()):
        print(f"The month name is {x}, and the month number is {month_number}")

print(year)
print(meeting_days)
