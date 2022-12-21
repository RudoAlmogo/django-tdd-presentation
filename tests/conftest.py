from datetime import datetime

import pytest

from restaurants.models import Restaurant


@pytest.fixture
def restaurant_valencia():
    return Restaurant.objects.create(
        name='Valencia',
        address='C/ Micer Mascó, 24, 46006, Valencia',
        opening_time=datetime.strptime('13:00', '%H:%M').time(),
        closing_time=datetime.strptime('23:00', '%H:%M').time(),
        active=True,
    )


@pytest.fixture
def restaurant_madrid():
    return Restaurant.objects.create(
        name='Madrid',
        address='C/ Micer Mascó, 24, 46006, Madrid',
        opening_time=datetime.strptime('12:00', '%H:%M').time(),
        closing_time=datetime.strptime('23:59', '%H:%M').time(),
        active=False,
    )
