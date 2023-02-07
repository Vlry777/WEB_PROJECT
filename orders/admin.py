from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'product', 'creation_time','payment_method')
 

    
     
    