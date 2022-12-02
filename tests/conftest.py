import pytest

from restaurants.models import Restaurant


@pytest.fixture
def restaurant_valencia():
    return Restaurant.objects.create(
        name='Valencia',
        address='C/ Micer Mascó, 24, 46006, Valencia',
        opening_time='13:00:00',
        closing_time='23:00:00',
        active=True,
    )


@pytest.fixture
def restaurant_madrid():
    return Restaurant.objects.create(
        name='Madrid',
        address='C/ Micer Mascó, 24, 46006, Madrid',
        opening_time='12:00:00',
        closing_time='23:59:00',
        active=False,
    )
