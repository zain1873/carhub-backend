from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CarFilter


# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['brand', 'city', 'fuel_type', 'transmission']
    filterset_class = CarFilter

    search_fields = ['name', 'description']
    ordering_fields = ['price', 'year', 'created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


