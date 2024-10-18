from django.contrib import admin
from .models import Post, Category, Contacto 
#Importamos de nuestro archivo models , el modelo 'post'
# Register your models here.

admin.site.register(Post) #Registramos en el admin la tabla post
admin.site.register(Category)
admin.site.register(Contacto)
