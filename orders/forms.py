from django import forms
from .models import Order

class OrdersForm(forms.Form):
    client = forms.CharField(label='Cliente',max_length=50)
    product = forms.CharField(label= 'Producto',max_length=100)
    creation_time= forms.DateTimeField(label='Fecha de creacion')
    payment_method = forms.ChoiceField(label= 'Metodo de pago', choices=Order.CHOICES)