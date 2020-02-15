from datetime import timedelta

from models.schedule import ScheduleItem


def test_schedule_item():
    schedule_item = ScheduleItem(name="run", time_length=0.5)
    assert schedule_item.name == "run"
    assert schedule_item.time_length == 0.5
