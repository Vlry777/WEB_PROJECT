from django.contrib.auth.models import User
from django.db import models


class Workshops(models.Model):
    workshop= models.OneToOneField(User, on_delete=models.CASCADE, related_name='workshop')#por que cambio el User? 
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    current = models.BooleanField(default=True)
    price = models.FloatField()
    workshop_image = models.ImageField(blank=True, null=True,upload_to= 'workshops_images')
    description = models.CharField(max_length=500)
