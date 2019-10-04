import random

class Thing():
    # where we're going to store the things
    things = {}

    def insert(self, value: any):
        self.things[len(self.things)] = value

    def delete(self, id: int):
        del self.things[id]

    def get_random(self):
        return self.things[random.randint(0, len(self.things) - 1)]

thing = Thing()
thing.insert('cats')
print(thing.things)
thing.insert('dogs')
thing.insert('birds')

for i in range(0, 4):
    print(thing.get_random())