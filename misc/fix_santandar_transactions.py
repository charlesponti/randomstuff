import json
import sys
from csv import DictReader, DictWriter
from getopt import GetoptError, getopt
from typing import List

data = None
file = None
transactions = []


def get_arguments(unixOptions: str, gnuOptions):
    try:
        return getopt(sys.argv[1:], unixOptions, gnuOptions)
    except GetoptError as err:
        raise OSError(f"Error getting arguments: {err}")


options, arguments = get_arguments("f:", ["file"])

for opt, arg in options:
    if opt == "-f":
        file = arg

if file:
    with open(file, "r") as file:
        data = DictReader(file)

        print(data.fieldnames)
        for row in data:
            transaction = dict(row)
            date: str = transaction["Date"]
            date_parts = date.split("/")
            transaction["Date"] = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
            transactions.append(transaction)

    with open("./fixed-transactions.csv", "w") as file:
        writer = DictWriter(file, data.fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    print(len(transactions))
    print(transactions[-1])
else:
    raise Warning("Please provide a -f with the path to the csv file")
