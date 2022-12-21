from datetime import datetime

import pytest
from freezegun import freeze_time

from ..models import Restaurant


@pytest.fixture
def restaurant():
    return Restaurant(
        name='Valencia',
        address='C/ Micer Mascó, 24, 46006, Valencia',
        opening_time=datetime.strptime('13:00', '%H:%M').time(),
        closing_time=datetime.strptime('23:00', '%H:%M').time(),
        active=True,
    )


def test_model_is_open_returns_false_when_not_active(restaurant: Restaurant):
    restaurant.active = False
    assert restaurant.is_open is False


@freeze_time('12:00')
def test_model_is_open_returns_false_when_active_but_not_in_hour_range(restaurant: Restaurant):
    assert restaurant.is_open is False


@freeze_time('13:00')
def test_model_is_open_returns_false_when_active_and_in_hour_range(restaurant: Restaurant):
    assert restaurant.is_open is True
