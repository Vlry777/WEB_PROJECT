from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=65)
    price= models.FloatField(default=0)
    amount= models.FloatField(default=0)
    subtotal= models.FloatField(default=0)
    total=models.FloatField(default=0)

    # def __str__(self):
    #     return f'{self.name}, {self.price}'




