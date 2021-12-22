from rest_framework import viewsets
import django_filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from .models import Town, Street, Store
from .serializers import TownSerializer, StreetSerializer, StoreSerializer


class TownViewSet(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StoreFilter(FilterSet):
    Name = django_filters.CharFilter(field_name='Name', lookup_expr='icontains')
    Comment = django_filters.CharFilter(field_name='Comment', lookup_expr='icontains')
    Town = django_filters.CharFilter(field_name='Street__Town__Name', lookup_expr='icontains')
    Street = django_filters.CharFilter(field_name='Street__Name', lookup_expr='icontains')
    Number = django_filters.CharFilter(field_name='Number', lookup_expr='icontains')

    class Meta:
        model = Store
        fields = ['Name', 'Comment', 'Town', 'Street', 'Number']


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = StoreFilter
