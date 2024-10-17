from django.db import models
from django.contrib.auth.models import User
import uuid 

# Crea tu modelo Category primero
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    descripcion = models.TextField(default='Sin descripción disponible')
    imagen_seccion = models.ImageField(null=True, blank=True, default="default_image.png")
    
    def __str__(self):
        return self.name

#Creamos una class Contacto

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    email = models.EmailField()
    asunto =  models.CharField(max_length=200)
    mensaje = models.TextField()

    def __str__(self):
        return f'{self.nombre_apellido} - {self.asunto}'

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen_seccion = models.ImageField(null=True, blank=True, default="default_image.png")
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)  # Cambia esto temporalmente
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    horario_atencion = models.CharField(max_length=100, blank=True)  # Horario de atención
    ubicacion = models.CharField(max_length=255, blank=True)  # Ubicación
    servicios = models.TextField(blank=True)  # Servicios ofrecidos (opcional)


    def __str__(self):
        return self.titulo

