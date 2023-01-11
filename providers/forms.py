from django import forms

class ProviderForm(forms.Form):
    name = forms.CharField(max_length=50)
    adress = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    email = forms.CharField()
    condition = forms.CharField(max_length=50)

