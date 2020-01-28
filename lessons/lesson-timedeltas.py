#
# Example file for working with timedelta objects
#

from datetime import date, datetime, time, timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print(f"The current date is {str(now)}")

# print today's date one year from now
print(f"one year from now will be: {str(now + timedelta(days=365))}")

# create a timedelta that uses more than one argument
print(f"The datetime in two weeks and 5 days is {str(now + timedelta(weeks=2, days=5))}")

# calculate the date 1 week ago, formatted as a string
one_week_ago = datetime.now() - timedelta(weeks=1)
print(f"One week ago it was {one_week_ago.strftime('%A %B %d %Y')}")

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    afd.replace(year = today.year + 1)
    print(f"The next April Fool's Day is {afd}")
else:
    print(f"The next April Fool's Day is {afd}")

# How many days have passed from the last April Fool's Day?
print(f"The last April Fools Day was {(today - afd.replace(today.year - 1)).days} days ago")

# Now calculate the amount of time until April Fool's Day
print(f"The next April Fool's Day is {(afd - today).days} days away")
