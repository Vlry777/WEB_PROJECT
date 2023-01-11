from django.urls import path

from providers.views import ProviderCreateView, ProvidersListView

urlpatterns= [
    path('provider-create/',ProviderCreateView.as_view(), name= 'providers-create'),
    path('providers-list/', ProvidersListView.as_view(), name='providers_list'),
]
   

