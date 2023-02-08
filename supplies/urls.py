from django.urls import path

from supplies.views import create_supplie, list_supplies, supplie_update, DeleteSupplie

urlpatterns = [
    path('create-supplie/',create_supplie),
    path('list-supplies/', list_supplies),
    path('update-supplies/<int:pk>/', supplie_update),
    path('delete-supplies/<int:pk>/', DeleteSupplie.as_view(),name='supplie_delete'),

]