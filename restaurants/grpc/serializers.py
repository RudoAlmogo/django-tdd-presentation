from django_socio_grpc import proto_serializers
from rest_framework import serializers

from ..models import Restaurant
from . import restaurants_pb2


class RestaurantProtoSerializer(proto_serializers.ModelProtoSerializer):
    is_open = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        proto_class = restaurants_pb2.RestaurantResponse
        proto_class_list = restaurants_pb2.RestaurantListResponse
        fields = ["id", "name", "opening_time", "closing_time", "is_open"]

    def get_is_open(self, obj) -> bool:
        return obj.is_open
