from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('title')
    serializer_class = ProductSerializer

    filterset_fields = ['title',] # поиск по атрибутам

    filter_backends = [DjangoFilterBackend, SearchFilter] # поиск по тексту
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().order_by('address')
    serializer_class = StockSerializer

    filterset_fields = ['products__id']
    '''
    В ЗАДАНИИ: поиск складов, где есть определенный продукт
GET {{baseUrl}}/stocks/?products=2

Не поняла, как это реализовать без __id, это опечатка или есть волшебный способ?)

    '''

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['products__title', 'products__description']
