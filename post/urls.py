from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('categoria/<uuid:categoria_id>/', views.post_list, name='post_list'),
    path('form_emprendimiento/', views.formulario, name = "FormEmp" ),
    
    

]