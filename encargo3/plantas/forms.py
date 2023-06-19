from django import forms
from .models import Productos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ProductoForm(forms.ModelForm):
    class Meta: 
        model = Productos
        fields = [ 'id', 'nombre', 'precio', 'descripcion','categoria', 'imagen']
        labels = {
            'id': 'id',
            'nombre' : 'nombre',
            'precio' : 'precio',
            'categoria' : 'Categoria', 
            'descripcion' :'Descripcion',
            'imagen': 'Imagen'
        }
        widgets ={
            'id': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese id..',
                    'id': 'id',
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre..',
                    'id': 'nombre',
                    'class': 'form-control'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese precio..',
                    'id': 'precio',
                    'class': 'form-control'
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese descripcion..',
                    'id': 'descripcion',
                    'class': 'form-control'
                }
            ), 
            'categoria': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese categoria..',
                    'id': 'categoria',
                    'class': 'form-control'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
            
        }
