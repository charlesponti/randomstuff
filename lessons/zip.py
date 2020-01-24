numbers = [1, 2, 3]
letters = ["a", "b", "c"]
zipped = zip(numbers, letters)

# Empty list
# print(zip())

# zip object
# print(zipped)

# <class 'zip'>
# print(type(zipped))

# list of tuples: [(numbers[0], letters[0]), ...]
# print(list(zipped))

# iterable will only be as long as shortest argument
# print(list(zip(['a', 'b', 'c'], [1,2,3,4])))

# can use itertools.zip_longest to retain trailing values
# from itertools import zip_longest
# zipped = zip_longest(numbers, letters, [1, 2, 3, 4, 5, 6], fillvalue='cats')
# print(list(zipped))

# dict of zipped values: { 'a': 1, 'b': 2, 'c': 3 }
# print(dict(zip(letters, numbers)))

# there is the ability to unpack zip as it generates tuples
# for l, n in zip(letters, numbers):
#     print(f'Letter: {l}')
#     print(f'Number: {n}')

# ability to iterate over dicts (ordered collections)
# dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
# dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
# print(dict_one.items())
# print(dict_two.items())
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# ability to seperate elements of tuples in a list of tuples
# pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# numbers, letters = zip(*pairs) # get two tuples of values
# print(pairs)
# print(*pairs)
# print(list(numbers))
# print(letters)

# ability to sort multiple lists
letters = ["b", "a", "c", "d"]
numbers = [3, 1, 2, 4]
data1 = list(zip(letters, numbers))
data2 = list(zip(numbers, letters))

data1.sort()
# print(data1) # sort by letters

data2.sort()
# print(data2)  # sort by numbers

# or use sorted, which can be used on any kind of sequence
# print(sorted(zip(letters, numbers)))

total_sales = [52000, 51000, 48000]
production_cost = [46800, 45900, 43200]
# for sales, cost in zip(total_sales, production_cost):
#     print(f"{sales} - {cost} = {sales - cost}")

# construct and update dicts
person_keys = ["name", "last_name", "age", "job"]
person_values = ["Jane", "Doe", 45, "Community Manager"]
person_dict = dict(zip(person_keys, person_values))
print(person_dict)
person_dict.update(zip(["job"], ["Python Developer"]))
print(person_dict)
