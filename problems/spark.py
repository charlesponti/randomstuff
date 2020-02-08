from functools import reduce
from logging import info
from typing import List

some_list = [1, 2, 3, 4, 5]


def get_bigger_numbers(limit):
    def is_bigger(itr: List, current_value: int):
        print(current_value, limit)
        if current_value < limit:
            itr.append(current_value)
        return itr

    return is_bigger


some_list_2 = map(lambda l: l + 1, some_list)
some_list_3 = reduce(get_bigger_numbers(3), some_list, [])

info(list(some_list_2))
info(list(some_list_3))
# print(add(1, 2))
