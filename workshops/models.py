
from django.db import models


class Workshops(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    current = models.BooleanField(default=True)
    price = models.FloatField()
    workshop_image = models.ImageField(upload_to= 'workshops_images',blank=True, null=True)
    description = models.CharField(max_length=500)
