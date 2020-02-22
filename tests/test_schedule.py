from datetime import timedelta

import pytest

from app.main.model.schedule import DuplicateError, Schedule, ScheduleItem


@pytest.fixture
def schedule():
    """Returns new Schedule"""
    return Schedule()


@pytest.fixture
def running():
    """Returns ScheduleItem with 'run' name and time_length of 30 mins"""
    return ScheduleItem(name="run", time_length=0.5)


def test_schedule_item(running):
    assert running.name == "run"
    assert running.time_length == 0.5


def test_schedule_add_to_daily(schedule, running):
    reading = ScheduleItem(name="reading", time_length=1)
    schedule.add_to_daily(running)
    schedule.add_to_daily(reading)
    assert len(schedule.daily) == 2


def test_schedule_add_to_daily_no_duplicates(schedule, running):
    schedule.add_to_daily(running)

    with pytest.raises(Exception):
        assert schedule.add_to_daily(running)

    assert len(schedule.daily) == 1
