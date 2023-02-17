from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=65)
    price= models.FloatField()
    amount= models.FloatField()
    subtotal= models.FloatField()
    total=models.FloatField()

    def __str__(self):
        return f'{self.name}, {self.price}'




