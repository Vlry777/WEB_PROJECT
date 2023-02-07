from django.shortcuts import render

from workshops.models import Workshops
from workshops.forms import WorkshopForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


@login_required
def create_workshop(request):
    if request.method == 'GET':
        context={
            'form':WorkshopForm()
        }

        return render(request,'workshops/create_workshop.html',context=context)
    
    elif request.method == 'POST':
        form = WorkshopForm(request.POST,request.FILES)
        if form.is_valid():
            Workshops.objects.create(
                name= form.cleaned_data['name'],
                date= form.cleaned_data['date'],
                current= form.cleaned_data['current'],
                price= form.cleaned_data['price'],
                description= form.cleaned_data['description'],
                workshop_image= form.cleaned_data['workshop_image'],
            )
            context={
                'message': 'Un nuevo Curso se ha creado!'
            }
            return render(request,'workshops/create_workshop.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': WorkshopForm()
            }
            return render(request, 'workshops/create_workshop.html', context=context)


def list_workshops(request):
    if 'search' in request.GET:
        search = request.GET['search']
        workshops = Workshops.objects.filter(name__incontains=search)
    else:
        workshops = Workshops.objects.all()
        context = {
            'workshops':workshops,
        }    
        return render(request,'workshops/list_workshops.html', context=context)

def workshop_update(request, pk):
    workshop = Workshops.objects.get(id=pk)
    if request.method == 'GET':
        context = {
            'form': WorkshopForm(
                initial={
                    'name':workshop.name,
                    'date':workshop.date,
                    'current':workshop.current,
                    'price':workshop.price,
                    'description':workshop.description,
                    'workshop_image':workshop.workshop_image
                }
            )
        }

        return render(request, 'workshops/update_workshop.html', context=context)

    elif request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            workshop.name = form.cleaned_data['name']
            workshop.date = form.cleaned_data['date']
            workshop.current = form.cleaned_data['current']
            workshop.price = form.cleaned_data['price']
            workshop.description = form.cleaned_data['description']
            workshop.workshop_image= form.cleaned_data['workshop_image']
            workshop.save()
            
            context = {
                'message': 'Curso actualizado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': WorkshopForm()
            }
        return render(request, 'workshops/update_workshop.html', context=context)


class DeleteWorkshop(DeleteView,PermissionRequiredMixin):
    model = Workshops
    success_url = '/workshops/list-workshops/'
    template_name = 'workshops/delete_workshop.html'