from django.shortcuts import render

from orders.models import Order
from orders.forms import OrdersForm



def create_order(request):
    if request.method == 'GET':
        context = {
            'form': OrdersForm()
        }

        return render(request, 'orders/create_order.html', context=context)

    elif request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                client=form.cleaned_data['client'],
                product=form.cleaned_data['product'],
                creation_time=form.cleaned_data['creation_time'],
                payment_method=form.cleaned_data['payment_method'],
            )
            context = {
                'message': 'Tu orden ha sido realizada!'
            }
            return render(request, 'orders/create_order.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': OrdersForm()
            }
            return render(request, 'orders/create_order.html', context=context)



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




