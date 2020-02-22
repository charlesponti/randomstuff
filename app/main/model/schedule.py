from datetime import date
from typing import Dict, List


class Day(date):
    pass


class ScheduleItem:
    # -- Name of activity
    name: str
    # -- Length of time in minutes
    time_length: float

    def __init__(self, *args, name: str = "", time_length: float = 0):
        self.name = name
        self.time_length = time_length


class DuplicateError(ValueError):
    pass


class Schedule:
    def __init__(self):
        self.daily: Dict = {}
        self.weekly: Dict = {}
        self.free_days: List[Day] = []

    def get_free_days(self) -> List[Day]:
        return self.free_days

    def add_to_daily(self, schedule_item: ScheduleItem):
        """Add to daily schedule

        :param schedule_item: ScheduleItem to add to daily schedule
        :type schedule_item: ScheduleItem
        :return: None
        """
        if self.daily.get(schedule_item.name) is not None:
            raise DuplicateError(
                f"'{schedule_item.name}' already part of daily schedule'"
            )
        else:
            self.daily[schedule_item.name] = schedule_item
