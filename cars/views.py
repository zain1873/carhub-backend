from django.shortcuts import render
from .serializers import CarSerializer
from .models import Car
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


