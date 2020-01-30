"""
I created this because when exporting transactions for Santander bank,
some dates are written as `DAY/MONTH/YEAR` which confuses spreadsheet
applications such as Google Sheets.

For example, if you attempt to format the Date column without converting these
date values, the spreadsheet application will attempt to find a month `25` and
day `12` for `25/12/2020`.
"""
import json
import sys
from csv import DictReader, DictWriter
from getopt import GetoptError, getopt
from typing import List


def get_arguments(unixOptions: str, gnuOptions):
    try:
        return getopt(sys.argv[1:], unixOptions, gnuOptions)
    except GetoptError as err:
        raise OSError(f"Error getting arguments: {err}")

def get_transactions_file():
    options, arguments = get_arguments("f:", ["file"])

    for opt, arg in options:
        if opt == "-f":
            file = arg

    if file:
        return file
    else:
        raise Warning("Please provide a -f with the path to the csv file")

def fix_transactions_dates(file: str):
    """
    Convert "DAY/MONTH/YEAR" to "YEAR-MONTH-DAY"
    """




if __name__ == "__main__":
    file = get_transactions_file()
    data = None
    transactions = []
    if file:
        fix_transactions_dates(file)
        with open(file, "r") as file:
            data = DictReader(file)
            for row in data:
                print(row)
                transaction = dict(row)
                date: str = transaction["Date"]
                day, month, year = date.split("/")
                transaction["Date"] = f"{year}-{month}-{day}"
                transactions.append(transaction)

        with open("./fixed-transactions.csv", "w") as file:
            writer = DictWriter(file, data.fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
