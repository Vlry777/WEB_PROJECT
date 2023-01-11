from django.shortcuts import render
from django.http import HttpResponse

from supplies.models import Supplies

from supplies.forms import SuplieForm

def create_product(request):
    if request.method == 'GET':
        context = {
            'form': SuplieForm()
        }

        return render(request, 'supplies/create_supplie.html', context=context)

    elif request.method == 'POST':
        form = SuplieForm(request.POST)
        if form.is_valid():
            Supplies.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'message': 'Se ha creado un insumo  exitosamente'
            }
            return render(request, 'supplies/create_supplie.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': SuplieForm()
            }
            return render(request, 'supplies/create_supplie.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        supplies = Supplies.objects.filter(name__icontains=search)
    else:
        supplies = Supplies.objects.all()
    context = {
        'supplies':supplies,
    }
    return render(request, 'supplies/list_supplies.html', context=context)

# def create_category(request, name):
#     Category.objects.create(name=name)
#     return HttpResponse('Categoria creada')

# def list_categories(request):
#     all_categories = Category.objects.all()
#     context = {
#         'categories':all_categories
#     }
#     return render(request, 'categories/list_categories.html', context=context)

