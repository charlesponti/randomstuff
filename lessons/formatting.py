#
# Example file for formatting time and date output
#

from datetime import datetime
import time


def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes
    now = datetime.now()

    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    # print(now.strftime("%a, %d %B, %y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    # print(now.strftime("Locale date and time: %c"))
    # print(now.strftime("Locale date: %x"))
    # print(now.strftime("Locale time: %X"))

    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    while True:
        print(datetime.now().strftime("Current time: %I:%M:%S %p"))
        time.sleep(1)
    # print(now.strftime("24-hour time: %H:%M"))


if __name__ == "__main__":
    main()
