from django_socio_grpc.utils.servicer_register import AppHandlerRegistry

from restaurants.grpc.services import RestaurantService


def grpc_handlers(server):
    app_registry = AppHandlerRegistry("restaurants", server)
    app_registry.register(RestaurantService)
