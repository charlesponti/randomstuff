from json import JSONEncoder
from csv import DictReader, DictWriter
import json
from classes import Person

person = Person("Chase", 33, "black")
data = JSONEncoder().encode(person.get())
field_names = ["name", "age", "hair"]

with open("./person.csv", "w", newline="") as file:
    writer = DictWriter(file, field_names)
    writer.writeheader()
    writer.writerow(person.get())

with open("./person.csv", "r") as file:
    data = DictReader(file)
    for row in data:
        print(row)
