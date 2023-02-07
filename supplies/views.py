from django.shortcuts import render

from supplies.models import Supplies
from supplies.forms import SupplieForm

def create_supplie(request):
    if request.method == 'GET':
        context = {
            'form': SupplieForm()
        }

        return render(request, 'supplies/create_supplie.html', context=context)

    elif request.method == 'POST':
        form = SupplieForm(request.POST,request.FILES)
        if form.is_valid():
            Supplies.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
                supplie_image= form.cleaned_data['supplie_image'],
            )
            context = {
                'message': 'Se ha creado un insumo  exitosamente'
            }
            return render(request, 'supplies/create_supplie.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': SupplieForm()
            }
            return render(request, 'supplies/create_supplie.html', context=context)

def list_supplies(request):
    if 'search' in request.GET:
        search = request.GET['search']
        supplies = Supplies.objects.filter(name__icontains=search)
    else:
        supplies = Supplies.objects.all()
    context = {
        'supplies':supplies,
    }
    return render(request, 'supplies/list_supplies.html', context=context)


