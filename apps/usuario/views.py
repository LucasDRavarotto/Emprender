from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class RegistroUsuarioForm(CreateView):
    template_name= 'registration/registrar.html'
    form_class = RegistroUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, inicia sesion.')
        form.save()

        return redirect('apps.usuario:registrar')
    
class LoginUsuario(LoginView):
    template_name= 'registration.login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login exitoso')

        return reverse('apps.usuario:login')
    

class LogoutUsuario(LogoutView):
    template_name= 'registration/lougout.html'

    def get_success_url(self):
        messages.success (self.request, 'Logout exitoso')

        return reverse ('apps.usuario:logout')