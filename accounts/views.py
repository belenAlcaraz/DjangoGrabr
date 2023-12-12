from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
"""
UserCreationForm,ya viene con Django y maneja la creación de nuevos usuarios. 
Después del registro exitoso,redirige a la página de inicio de sesión (login) 
utilizando reverse_lazy
"""

class UsuarioRegistroView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
