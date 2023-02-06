from django import forms

class WorkshopForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateTimeField()
    current = forms.BooleanField(required= False)
    price = forms.FloatField()
    description = forms.CharField()
