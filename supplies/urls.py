from django.urls import path

from supplies.views import create_supplie, list_supplies

urlpatterns = [
    path('create-supplie/',create_supplie),
    path('list-supplies/', list_supplies),
]