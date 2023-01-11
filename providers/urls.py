from django.urls import path

from providers.views import ProviderCreateView, providers_list

urlpatterns= {
    path('provider-create/',ProviderCreateView.as_view(), name= 'providers-create'),
    path('providers-list/',providers_list),
}