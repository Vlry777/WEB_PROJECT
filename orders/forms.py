from django import forms

class OrdersForm(forms.Form):
    client = forms.CharField(max_length=50)
    product = forms.CharField(max_length=100)
    creation_time= forms.DateTimeField()
    payment_method = forms.CharField()