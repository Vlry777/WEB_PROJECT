from django.urls import path

from orders.views import create_order,list_orders

urlpatterns = [ 
    path('create-order/', create_order), 
    path('list-orders/', list_orders),
    ]
  
