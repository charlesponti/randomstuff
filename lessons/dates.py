#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print(today)

    # print out the date's individual components
    print(today.year, today.month, today.day)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    weekday = today.weekday()
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    print("Today is", days[today.weekday()], "and it's weekday number is", weekday)

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    now = datetime.now()
    print("The current date and time is", now)

    # Get the current time
    t = datetime.time(datetime.now())
    print("The time is", t)


if __name__ == "__main__":
    main()
