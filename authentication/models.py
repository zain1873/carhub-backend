from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone


class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def is_expired(self):
        return self.created_at < timezone.now() - timedelta(minutes=10)