from django.shortcuts import render
from django.http import HttpResponse

from orders.models import Order


def list_orders(request):
    if 'search' in request.GET:
        search = request.GET['search']
        orders = Order.objects.filter(name__icontains=search)
    else:
        orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'orders/list_orders.html', context=context)

def create_order(request):
    Order.objects.create(client='Franco', buy='Compra $10000', creation_time= 10/1/2023,payment_method='Cash')
    return HttpResponse('Order created')


