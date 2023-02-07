from django.db import models

class Supplies(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    supplie_image = models.ImageField(upload_to='Supplies_images',blank=True, null=True)

    def __str__(self):
        return f"Nombre: {self.name} - Precio:{self.price} - Stock:{self.stock} - Imagen de insumo:{self.supplie_image}"
