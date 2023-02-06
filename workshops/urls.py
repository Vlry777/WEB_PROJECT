from django.urls import path

from workshops.views import create_workshop,list_workshops

urlpatterns = [
    path('create-workshop/', create_workshop),
    path('list-workshops/', list_workshops),
]