from typing import List
from datetime import date


class Day(date):
    pass


class Schedule:
    free_days: List[Day] = []

    def get_free_days(self) -> List[Day]:
        return self.free_days
