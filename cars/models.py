from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Car(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Cars')
  name = models.CharField(max_length=200)
  car_model = models.IntegerField()
  milage = models.IntegerField()
  year = models.IntegerField(default=timezone.now().year)
  price = models.DecimalField(max_digits=20, decimal_places=2)
  brand = models.CharField(max_length=50)
  color = models.CharField(max_length=30, blank=True, null=True)
  fuel_type = models.CharField(max_length=50, choices=[('petrol','Petrol'), ('diesel','Diesel'), ('electric','Electric')])
  transmission = models.CharField(max_length=50, choices=[('manual','Manual'), ('automatic','Automatic')])
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  likes = models.PositiveIntegerField(default=0)
  views = models.PositiveIntegerField(default=0)
  updated_at = models.DateTimeField(auto_now=True)
  city = models.CharField(max_length=100) 
  status = models.CharField(max_length=50, choices=[('available','Available'), ('sold','Sold')], default='available')
  image = models.ImageField(upload_to="cars/", null=True, blank=True)

  def __str__(self):
        return f"{self.brand} {self.name} ({self.car_model})"



