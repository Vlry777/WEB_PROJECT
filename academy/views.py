from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={})

def about_us(request):
    return render(request,'about_us.html', context={})

