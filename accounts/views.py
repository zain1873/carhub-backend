from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response  
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None): 
        profile = request.user.profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def update(self, request, pk=None):
        profile = request.user.profile
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)