from django.db import models
from django.contrib.auth.models import User


class Ride(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  