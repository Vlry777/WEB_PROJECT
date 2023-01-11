from django.views.generic import ListView, CreateView
from django.shortcuts import render

from providers.models import Provider

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/provider-create.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'


class ProvidersListView(ListView):
    model = Provider
    template_name = 'providers/providers-list.html'
    queryset = Provider.objects.filter(is_active = True)
  
