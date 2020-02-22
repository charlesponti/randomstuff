
class Category():
    tag: str = ''

    def __init__(self, tag: str):
        self.tag = tag

categories = [
    'work',
    'finance',
    'subscription',
    'entertainment',
    'groceries',
    'dining out'
]

converted_categories = []

for category in categories:
    converted_categories.append(Category(tag=category))

print(converted_categories[0].tag)