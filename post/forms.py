from django.forms import ModelForm
from django import forms
from .models import Post , Category, Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre_apellido", "email", "asunto", "mensaje"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'imagen_seccion', 'imagen_detalle', 'horario_atencion', 'ubicacion', 'servicios', 'email_contacto', 'telefono_contacto']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

