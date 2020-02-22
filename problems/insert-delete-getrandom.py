import random
from typing import Any, Dict


class Collection:
    # where we're going to store the things
    data: Dict = {}

    def insert(self, value: any):
        self.data[len(self.data)] = value

    def delete(self, id: int):
        del self.data[id]

    def get_random(self):
        return self.data[random.randint(0, len(self.data) - 1)]


collection = Collection()
collection.insert("cats")
print(collection.data)

collection.insert("dogs")
collection.insert("birds")

for i in range(0, 4):
    print(collection.get_random())
