from django_socio_grpc import proto_serializers

from ..models import Restaurant
from . import restaurants_pb2


class RestaurantProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Restaurant
        proto_class = restaurants_pb2.RestaurantResponse
        proto_class_list = restaurants_pb2.RestaurantListResponse
        fields = ["id", "name"]
