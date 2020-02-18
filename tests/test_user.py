import pytest

from app.main.model.user import User


@pytest.fixture
def user():
    return User()


def test_update_reading_speed(user):
    assert user.reading_speed == 0
    user.update_reading_speed(50)
    assert user.reading_speed == 50
