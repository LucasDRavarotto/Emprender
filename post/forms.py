from django.forms import ModelForm
from django import forms
from .models import Post , Category

class PostForm(ModelForm): 
    class Meta: 
        model = Post 
        fields = '__all__'
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
