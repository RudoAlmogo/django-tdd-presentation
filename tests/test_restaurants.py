from django.test import Client

from restaurants.models import Restaurant


def test_get_resturants_returns_list_of_restaurants(
    client: Client, restaurant_valencia: Restaurant, restaurant_madrid: Restaurant
):
    response = client.get('/restaurants/')

    assert response.status_code == 200
    assert response.json() == [
        {
            'id': restaurant_valencia.id,
            'name': restaurant_valencia.name,
            'address': restaurant_valencia.address,
            'opening_time': str(restaurant_valencia.opening_time),
            'closing_time': str(restaurant_valencia.closing_time),
            'is_open': restaurant_valencia.is_open,
        },
        {
            'id': restaurant_madrid.id,
            'name': restaurant_madrid.name,
            'address': restaurant_madrid.address,
            'opening_time': str(restaurant_madrid.opening_time),
            'closing_time': str(restaurant_madrid.closing_time),
            'is_open': restaurant_madrid.is_open,
        },
    ]
