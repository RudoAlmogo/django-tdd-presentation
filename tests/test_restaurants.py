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
            'opening_time': restaurant_valencia.opening_time,
            'closing_time': restaurant_valencia.closing_time,
            'active': restaurant_valencia.active,
        },
        {
            'id': restaurant_madrid.id,
            'name': restaurant_madrid.name,
            'address': restaurant_madrid.address,
            'opening_time': restaurant_madrid.opening_time,
            'closing_time': restaurant_madrid.closing_time,
            'active': restaurant_madrid.active,
        },
    ]
