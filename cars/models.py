from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Car model — main listing
class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    
    # Step 1: Basic Info
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=30, blank=True, null=True)
    car_model = models.IntegerField(help_text="Car model or version")
    year = models.IntegerField(default=timezone.now().year)
    city = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    fuel_type = models.CharField(max_length=50, choices=[('petrol','Petrol'), ('diesel','Diesel'), ('electric','Electric')])
    transmission = models.CharField(max_length=50, choices=[('manual','Manual'), ('automatic','Automatic')])
    description = models.TextField()
    
    # Step 2: Specifications
    engine_size = models.DecimalField(max_digits=4, decimal_places=1, default=1.6, help_text="Engine size in Liters (e.g. 1.8)")  
    doors = models.PositiveIntegerField(choices=[(2,"2 Doors"), (4,"4 Doors")])
    seats = models.PositiveIntegerField(choices=[(2,"2 Seats"),(4,"4 Seats"),(5,"5 Seats"),(6,"6 Seats"),(7,"7 Seats"),(8,"8 Seats")])
    milage = models.IntegerField(help_text="Mileage in km/l")

    # Step 3: Images (main image)
    image = models.ImageField(upload_to="cars/", null=True, blank=True)

    # Optional Features
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    # Step 4: Status
    DRAFT = 'draft'
    AVAILABLE = 'available'
    SOLD = 'sold'
    STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (AVAILABLE, 'Available'),
        (SOLD, 'Sold'),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=DRAFT)

    # Optional Buyer info
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchased_cars')

    def __str__(self):
        return f"{self.brand} {self.name} ({self.car_model})"


# Optional: Multiple images per car
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="cars/")
    uploaded_at = models.DateTimeField(auto_now_add=True)