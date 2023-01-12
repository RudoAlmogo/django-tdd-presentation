import django_filters as filters
from django.db.models import QuerySet

from .models import Restaurant


class RestaurantFilter(filters.FilterSet):
    names = filters.CharFilter(field_name='name', method='attribute_in_list')

    class Meta:
        model = Restaurant
        fields = ('names',)

    def attribute_in_list(self, queryset: QuerySet[Restaurant], name: str, value: str):
        return queryset.filter(**{f'{name}__in': value.split(',')})
