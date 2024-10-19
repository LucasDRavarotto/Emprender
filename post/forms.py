from django.forms import ModelForm
from django import forms
from .models import Post , Category, Contacto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre_apellido", "email", "asunto", "mensaje"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'imagen_seccion', 'imagen_detalle', 'horario_atencion', 'ubicacion', 'servicios', 'email_contacto', 'telefono_contacto', 'link1', 'link2']
                
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']   