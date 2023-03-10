from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView
from django.shortcuts import render

from providers.models import Provider

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/provider-create.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'


class ProvidersListView(LoginRequiredMixin, ListView):
    model = Provider
    template_name = 'providers/providers-list.html'
    queryset = Provider.objects.filter(is_active = True)

    def providers_list(request):
        if 'search' in request == 'GET':
            search = request.GET['search']
            providers = Provider.objects.filter(name__contains= search)
        else:
            providers = Provider.objects.all()
        context = {
            'providers': providers,
        }
        return render(request,'providers/providers_list.html', context=context)
    
  
