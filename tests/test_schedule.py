from datetime import timedelta

from models.schedule import Schedule, ScheduleItem

global schedule
global running

schedule = None
running = None


def setup():
    schedule = Schedule()
    running = ScheduleItem(name="run", time_length=0.5)


def test_schedule_item():
    assert running.name == "run"
    assert running.time_length == 0.5


def test_schedule_add_to_daily():
    running = ScheduleItem(name="run", time_length=0.5)
    reading = ScheduleItem(name="reading", time_length=1)
    schedule.add_to_daily(running)
    schedule.add_to_daily(reading)
    assert len(schedule.daily) == 2


def test_schedule_add_to_daily_no_duplicates():
    schedule = Schedule()
    running = ScheduleItem(name="run", time_length=0.5)
    schedule.add_to_daily(running)
    schedule.add_to_daily(running)
    assert len(schedule.daily) == 1


def teardown():
    print("finished")
