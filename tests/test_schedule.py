from datetime import timedelta

from models.schedule import Schedule, ScheduleItem


def test_schedule_item():
    schedule_item = ScheduleItem(name="run", time_length=0.5)
    assert schedule_item.name == "run"
    assert schedule_item.time_length == 0.5


def test_schedule_add_to_daily():
    schedule = Schedule()
    running = ScheduleItem(name="run", time_length=0.5)
    reading = ScheduleItem(name="reading", time_length=1)
    schedule.add_to_daily(running)
    schedule.add_to_daily(running)
    assert len(schedule.daily) == 2
