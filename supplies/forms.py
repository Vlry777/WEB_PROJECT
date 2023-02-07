from django import forms

class SupplieForm(forms.Form):
    name = forms.CharField(label='Nombre',max_length=100,required=True)
    price = forms.FloatField(label='Precio',required=True)
    stock = forms.BooleanField(label='Stock',required=False)
    supplie_image= forms.ImageField(label='Imagen del insumo',required=True)