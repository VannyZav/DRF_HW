from django.shortcuts import render
from rest_framework import viewsets, request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import ApiUser, Warehouse, Product
from api.serializers import UserSerializer, WareHouseSerializer, ProductSerializer


# Create your views here.

class ApiUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = ApiUser.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', "patch"]

class WareHouseModelViewSet(viewsets.ModelViewSet):
    serializer_class = WareHouseSerializer
    queryset = Warehouse.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', "patch"]


class ProductModelViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', "patch"]

class ProductApiView(APIView):
    ...
