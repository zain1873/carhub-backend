from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter
from .permissions import IsOwnerOrReadOnly  
from rest_framework.decorators import action
from rest_framework.response import Response
from .pagination import CarPagination


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'city', 'fuel_type', 'transmission']
    filterset_class = CarFilter
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'year', 'created_at']
    pagination_class = CarPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # 🔹 My Cars endpoint
    @action(detail=False, methods=['get'], url_path='my-cars')
    def my_cars(self, request):
        user_cars = Car.objects.filter(owner=request.user)
        serializer = self.get_serializer(user_cars, many=True)
        return Response(serializer.data)