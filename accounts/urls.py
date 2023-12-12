from django.urls import path
from accounts.views import UsuarioRegistroView


urlpatterns = [
   path('registro/',UsuarioRegistroView.as_view(),name='Registro'),
   

]

