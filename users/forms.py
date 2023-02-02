from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required= True, label='Nombre')
    last_name = forms.CharField(max_length=50, required= True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required= True, label='Nombre de Usuario')
    first_name = forms.CharField(max_length=50, required= True, label='Nombre')
    last_name = forms.CharField(max_length=50, required= True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name']

