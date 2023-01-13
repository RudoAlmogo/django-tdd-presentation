import logging

import grpc

from restaurants.grpc import restaurants_pb2, restaurants_pb2_grpc


def run():
    with grpc.insecure_channel('127.0.0.1:8000') as channel:
        stub = restaurants_pb2_grpc.RestaurantControllerStub(channel)

        # Retrieve restaurant
        request = restaurants_pb2.RestaurantRetrieveRequest(id=1)
        restaurant = stub.Retrieve(request)
        print(f'TYPE: {type(restaurant)}')
        print(f'ID: {restaurant.id}')
        print(f'NAME: {restaurant.name}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
