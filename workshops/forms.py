from django import forms
from workshops.models import Workshops

class WorkshopForm(forms.Form):
    name = forms.CharField(label= 'Nombre',max_length=100, required=True)
    date = forms.DateTimeField(label= 'Fecha',required=True)
    current = forms.BooleanField(label= 'Vigente',required=True)
    price = forms.FloatField(label='Precio',required=True)
    workshop_image = forms.ImageField(label= 'Imagen del curso',required=True)
    description = forms.CharField(label= 'Descripción',max_length=500,required=True)
