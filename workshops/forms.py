from django import forms
from workshops.models import Workshops

class WorkshopForm(forms.ModelForm):
    class Meta:
        model= Workshops
        fields= ['name','date','current','price','description','workshop_image']
        label={
            'name':'Nombre',
            'date':'Fecha',
            'current':'Vigente',
            'price':'Precio',
            'description':'Descripcion',
            'workshop_image': 'Imagen del curso',
        }
