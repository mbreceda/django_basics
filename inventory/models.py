import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=200)
    doors = models.IntegerField()
    lot_number = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.make} - {self.model}"




