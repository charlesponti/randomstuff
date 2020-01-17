#
# Example file for working with date information
#
from datetime import date
import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  print(date.today())

  # print out the date's individual components
  today = date.today()
  print(today.year, today.month, today.day)

  # retrieve today's weekday (0=Monday, 6=Sunday)
  print(today.weekday())

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print(datetime.date.today())

  # Get the current time
  print()

if __name__ == "__main__":
  main();
