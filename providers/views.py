from django.views.generic import ListView, CreateView
from django.shortcuts import render

from providers.models import Provider
from providers.forms import ProviderForm


class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/provider-create.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'


def providers_list(request):
    providers = Provider.objects.filter(is_active = True)
    context = {
        'providers':providers
    }
    return render(request, 'providers/providers-list.html', context=context)
  
