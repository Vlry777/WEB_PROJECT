from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from workshops.models import Workshops
from workshops.forms import WorkshopForm

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