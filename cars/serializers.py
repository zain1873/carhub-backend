from .models import Car
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')  # show username

    class Meta:
      model = Car         
      fields = '__all__' 