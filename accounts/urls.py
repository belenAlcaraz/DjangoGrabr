from django.urls import path
from accounts.views import UsuarioRegistroView, ViajeroPerfilView, CompradorPerfilView


urlpatterns = [
   path('registro/',UsuarioRegistroView.as_view(),name='Registro'),
   path('viajero/<int:pk>/', ViajeroPerfilView.as_view(), name='Viajero_perfil'),
   path('comprador/<int:pk>/', CompradorPerfilView.as_view(), name='Comprador_perfil'),
   

]

