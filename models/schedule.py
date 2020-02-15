from typing import List


class ScheduleItem:
    # -- Name of activity
    name: str
    # -- Length of time in minutes
    time_length: float

    def __init__(self, *args, name: str = "", time_length: float = 0):
        self.name = name
        self.time_length = time_length


class Schedule:
    daily: List[ScheduleItem] = []
    weekly: List[ScheduleItem] = []

    def add_to_daily(self, schedule_item: ScheduleItem):
        self.daily.append(schedule_item)
