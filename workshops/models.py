
from django.db import models


class Workshops(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    current = models.BooleanField(default=True)
    price = models.FloatField()
    workshop_image = models.ImageField(upload_to= 'workshops_images',blank=True, null=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"Nombre: {self.name} - Fecha:{self.date} - Vigente:{self.current} - Precio:{self.price} \
            - Imagen del curso:{self.workshop_image} - Descripcion:{self.description}"
