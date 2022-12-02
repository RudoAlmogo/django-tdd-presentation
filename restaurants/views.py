from rest_framework import mixins, viewsets

from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
