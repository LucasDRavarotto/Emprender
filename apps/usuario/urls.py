from django.urls import path
from . import views
from .views import LoginUsuario, RegistroUsuarioForm
from django.contrib.auth import views as auth_views
app_name = 'apps.usuario'

urlpatterns= [ 
    path('registrar/', views.RegistroUsuarioForm.as_view(), name= 'registrar'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('logout/', views.LogoutUsuario.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name= 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name= 'password_reset_complete'),
    ]
