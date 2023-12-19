from django.views import generic
from django.views.generic import DetailView,TemplateView,ListView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm
from accounts.models import Comprador, Viajero
from delivery.models import Producto, OfertaDeEntrega


"""
UserCreationForm,ya viene con Django y maneja la creación de nuevos usuarios. 
Después del registro exitoso,redirige a la página de inicio de sesión (login) 
utilizando reverse_lazy
"""

class UsuarioRegistroView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ViajeroPerfilView(DetailView):
    model = Viajero
    template_name = 'viajero_perfil.html'
    context_object_name = 'viajero'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        viajero = self.request.user.viajero
        context['viajero'] = viajero

        ofertas_pendientes = OfertaDeEntrega.objects.filter(viajero=viajero, estado='pendiente').count()
        ofertas_aceptadas = OfertaDeEntrega.objects.filter(viajero=viajero, estado='aceptado').count()
        ofertas_rechazadas = OfertaDeEntrega.objects.filter(viajero=viajero, estado='cancelado').count()
        ofertas_entregadas = OfertaDeEntrega.objects.filter(viajero=viajero, estado='entregado').count()

        context['ofertas_pendientes'] = ofertas_pendientes 
        context['ofertas_aceptadas'] = ofertas_aceptadas
        context['ofertas_rechazadas'] = ofertas_rechazadas
        context['ofertas_entregadas'] = ofertas_entregadas

        return context
    
class CompradorPerfilView(TemplateView):
    template_name = 'comprador_perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comprador = self.request.user.comprador  # Asegúrate de que el usuario sea un comprador
        context['comprador'] = comprador

        # Obtén el conteo de productos en cada estado para el comprador
        context['pendientes_count'] = Producto.objects.filter(usuario=comprador, estado='pendiente').count()
        context['en_proceso_count'] = Producto.objects.filter(usuario=comprador, estado='en proceso').count()
        context['completados_count'] = Producto.objects.filter(usuario=comprador, estado='completado').count()
        context['cancelados_count'] = Producto.objects.filter(usuario=comprador, estado='cancelado').count()

        return context