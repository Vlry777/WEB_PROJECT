from django.urls import path

from workshops.views import create_workshop,list_workshops,workshop_update,DeleteWorkshop

urlpatterns = [
    path('create-workshop/', create_workshop),
    path('list-workshops/', list_workshops),
    path('update-workshops/<int:pk>/', workshop_update),
    path('delete-workshops/<int:pk>/', DeleteWorkshop.as_view(),name='workshop_delete'),

]