from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework import viewsets, request, generics, mixins, permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.models import ApiUser, Warehouse, Product
from api.serializers import UserSerializer, WareHouseSerializer, ProductSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # Разрешить доступ на изменение только владельцу объекта
        return obj == request.user

# Create your views here.
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешить доступ только администраторам для всех действий
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Разрешить доступ только администраторам для изменения объекта
        return request.user and request.user.is_staff

class IsSupplierOrConsumer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.user_type == 'supplier' or request.user.user_type == 'consumer')

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update']:
            return True
        return False


class ApiUserModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = ApiUser.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', "patch"]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAdminUser() or IsOwner()]
        elif self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action in ['retrieve']:
            return [IsAdminUser() or IsOwner()]
        elif self.action in ['list']:
            return [IsAdminUser()]
        return [permissions.AllowAny()]


class WareHouseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = WareHouseSerializer
    queryset = Warehouse.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', "patch"]


class ProductModelViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', "patch"]

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsSupplierOrConsumer()]
        elif self.action == 'create':
            return [IsAdminUser()]
        elif self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        elif self.action == 'destroy':
            return [IsAdminUser()]
        return [permissions.AllowAny()]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        user_type = request.user.user_type

        if user_type == 'supplier':
            if int(request.data.get('count', 0)) < 0:
                return Response({'error': 'You can write only positive num'}, status=status.HTTP_400_BAD_REQUEST)
            instance.count += int(request.data.get('count', 0))
        elif user_type == 'consumer':
            if int(request.data.get('count', 0)) < 0:
                return Response({'error': 'You can write only positive num'}, status=status.HTTP_400_BAD_REQUEST)
            count = int(request.data.get('count', 0))
            if instance.count >= count:
                instance.count -= count
            else:
                return Response({'error': 'Not enough products in stock'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User type not allowed to update product count'}, status=status.HTTP_403_FORBIDDEN)

        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect('/')


