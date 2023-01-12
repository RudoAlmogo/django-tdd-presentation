from rest_framework import mixins, viewsets

from .filters import RestaurantFilter
from .models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilter
