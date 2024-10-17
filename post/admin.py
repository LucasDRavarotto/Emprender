from django.contrib import admin
from .models import Post, Categoria #Importamos de nuestro archivo models , el modelo 'post'
# Register your models here.

admin.site.register(Post) #Registramos en el admin la tabla post
admin.site.register(Categoria)