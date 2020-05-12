from django.db import models

# Create your models here.
class Event(models.Model):
    googleId = models.CharField(max_length = 50, null=True)
    summary = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
