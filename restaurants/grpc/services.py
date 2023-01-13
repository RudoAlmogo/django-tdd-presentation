from django_socio_grpc import generics

from ..models import Restaurant
from .serializers import RestaurantProtoSerializer


class RestaurantService(generics.AsyncListService, generics.AsyncRetrieveService):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantProtoSerializer
