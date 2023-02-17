from django.urls import path

from shoppingcart.views import shop

urlpatterns=[
    path('shop/',shop),
]