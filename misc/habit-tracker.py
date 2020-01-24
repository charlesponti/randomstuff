from typing import NamedTuple, List

frequencies: List[NamedTuple] = [
    ("EVERY_DAY", "some_value"),
    ("EVERY_YEAR", "some_value"),
]


class Habit:
    action: str
    frequency: str

casts = "foo"
habits: List[Habit] = [{"action": "read 60 pages", "frequency": "EVERY_DAY"}]
