import json
from csv import DictReader
import sys
from getopt import getopt, GetoptError

file = None
transactions = []

def get_arguments(unixOptions: str, gnuOptions):
    try:
        return getopt(sys.argv[1:], unixOptions, gnuOptions)
    except GetoptError as err:
        print(f"Error getting arguments: {err}")

options, arguments = get_arguments("f:", ["file"])

for opt, arg in options:
    if (opt == "-f"):
        file = arg

if file:
    with open(file, "r") as file:
        data = DictReader(file)
        for row in data:
            transactions.append(row)
    print(len(transactions))