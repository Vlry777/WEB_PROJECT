from django.db import models

class Workshops(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    current = models.BooleanField(default=True)
    price = models.FloatField()
    image = models.ImageField(upload_to= 'Workshops_images')
    description = models.CharField(max_length=300)
