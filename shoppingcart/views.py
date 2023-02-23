from django.shortcuts import render,redirect

from .trolley import Trolley

from shoppingcart.models import Product


def shop(request):
    products= Product.objects.all()

    return render(request,'shoppingcart/trolley.html',products= products)


def add_product(request, product_id):
    trolley = Trolley(request)
    product= Product.objects.get(id= product_id)
    trolley.add(product=product)
    return redirect('shop')

def delete_product(request, product_id):
    trolley = Trolley(request)
    product= Product.objects.get(id= product_id)
    trolley.delete(product=product)
    return redirect('shop')

def subtract_product(request, product_id):
    trolley = Trolley(request)
    product= Product.objects.get(id= product_id)
    trolley.subtract_product(product=product)
    return redirect('shop')

def clear_trolley(request):
    trolley = Trolley(request)
    trolley.clear_trolley()
    return redirect('shop')





































