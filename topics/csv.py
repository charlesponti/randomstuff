# class Person:
#   def __init__(self, name: str, age: int, hair: str, **kwargs):
#     self.name = name
#     self.age = age
#     self.hair = hair

#   def get(self):
#     return {
#       'name': self.name,
#       'age': self.age,
#       'hair': self.hair
#     }

# person = Person("Chase", 33, "black")
# data = JSONEncoder().encode(person.get())

# with open('./persondb.txt', 'a') as file:
#   file.write(data)

# with open('./persondb.txt', 'r') as file:
#   print(file.read())

# field_names = ['name', 'age', 'hair']

# with open('./person.csv', 'w', newline='') as file:
#   writer = DictWriter(file, field_names)
#   writer.writeheader()
#   writer.writerow(person.get())

# with open('./person.csv', 'r') as file:
#   data = DictReader(file)
#   for row in data:
#     print(row)