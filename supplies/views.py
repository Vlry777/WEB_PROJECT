from django.shortcuts import render

from supplies.models import Supplies
from supplies.forms import SupplieForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import DeleteView

@login_required
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


def supplie_update(request, pk):
    supplie = Supplies.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form': SupplieForm(
                initial={
                    'name':supplie.name,
                    'price':supplie.price,
                    'stock':supplie.stock,
                    'supplie_image':supplie.supplie_image
                }
            )
        }

        return render(request, 'supplies/update_supplie.html', context=context)

    elif request.method == 'POST':
        form = SupplieForm(request.POST, request.FILES)
        if form.is_valid():
            supplie.name = form.cleaned_data['name']
            supplie.price = form.cleaned_data['price']
            supplie.stock = form.cleaned_data['stock']
            supplie.supplie_image= form.cleaned_data['supplie_image']
            supplie.save()
            
            context = {
                'message': 'Insumo actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': SupplieForm()
            }
        return render(request, 'supplies/update_supplie.html', context=context)


class DeleteSupplie(DeleteView,PermissionRequiredMixin):
    model = Supplies
    success_url = '/supplies/list-supplies/'
    template_name = 'supplies/delete_supplie.html'


