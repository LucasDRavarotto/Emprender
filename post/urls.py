from django.urls import path
from . import views
from .views import home, post_detail, contacto_view
from uuid import UUID

urlpatterns = [ 
    path('', views.home, name="home"),
    path('categoria/<uuid:categoria_id>/', views.post_list, name='post_list'),
    path('form_emprendimiento/', views.formulario, name = "FormEmp" ),
    path('<uuid:post_id>/', post_detail, name='post_detail'),
    path('buscar/', views.buscar_posts, name='buscar_posts'),
    path('contacto/', contacto_view, name='contacto'),
    
]