from .models import Car
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)  
    owner_username = serializers.ReadOnlyField(source='owner.username') 

    class Meta:
        model = Car
        fields = '__all__'