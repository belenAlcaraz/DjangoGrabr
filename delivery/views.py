from django.forms.models import ModelForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,CreateView, DetailView
from .models import Producto, OfertaDeEntrega
from .forms import ProductoForm, OfertaDeEntregaForm

class InicioView(ListView):
    model = Producto
    template_name = 'inicio.html'
    context_object_name = 'productos'

class ComprarProductoView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'comprar.html'
    success_url = reverse_lazy('Lista_producto')

    def form_valid(self, form: ModelForm):
        form.instance.usuario = self.request.user.comprador
        return super().form_valid(form)

class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'compra_detalle.html' 
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        context['es_comprador'] = self.request.user == producto.usuario
        context['ofertas'] = OfertaDeEntrega.objects.filter(producto=producto)
        return context

class ListaProductosView(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'
    ordering = ['-id']

class OfertaView(CreateView):
    model =  OfertaDeEntrega
    form_class = OfertaDeEntregaForm
    template_name = 'hacer_oferta_entrega.html'
    success_url = reverse_lazy('Pedidos_viajero')

    def form_valid(self, form):
        producto_pk = self.kwargs['pk']
        producto = get_object_or_404(Producto, pk=producto_pk)
        form.instance.producto = producto
        form.instance.viajero = self.request.user.viajero
        self.producto_pk = producto_pk
        return super().form_valid(form)
   
class PedidosViajeroView(ListView):
    model = Producto
    template_name = 'pedidos_viajero.html'
    context_object_name = 'productos'
  
class OfertasViajeroView(ListView):
    model= Producto
    template_name = 'tus_ofertas.html'
    context_object_name = 'productos'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        viajero = self.request.user.viajero
        context['viajero'] = viajero

        ofertas = OfertaDeEntrega.objects.filter(viajero=viajero)

        ofertas_pendientes = ofertas.filter(estado='pendiente')
        ofertas_aceptadas = ofertas.filter(estado='aceptado')
        ofertas_en_proceso = ofertas.filter(estado='en proceso')
        ofertas_completadas = ofertas.filter(estado='entregado')
        ofertas_canceladas = ofertas.filter(estado='cancelado')

        context['ofertas_pendientes'] = ofertas_pendientes
        context['ofertas_aceptadas'] = ofertas_aceptadas
        context['ofertas_en_proceso'] = ofertas_en_proceso
        context['ofertas_completadas'] = ofertas_completadas
        context['ofertas_canceladas'] = ofertas_canceladas

        return context

class CompraDetalleViajero(DetailView):
    model = Producto
    template_name = 'compra_detalle_viajero.html'

def aceptar_oferta(request, oferta_id):
    oferta = get_object_or_404(OfertaDeEntrega, id=oferta_id)
    oferta.estado = 'aceptado'
    oferta.save()
    producto = oferta.producto
    producto.estado = 'en proceso'  
    producto.save()
    detalle_producto_url = reverse('Detalle_producto', kwargs={'pk': oferta.producto.pk})
    return HttpResponseRedirect(detalle_producto_url)

def rechazar_oferta(request, oferta_id):
    oferta = get_object_or_404(OfertaDeEntrega, id=oferta_id)
    oferta.estado = 'cancelado'
    oferta.save()
    producto = oferta.producto
    producto.estado = 'cancelado'  
    producto.save()
    detalle_producto_url = reverse('Detalle_producto', kwargs={'pk': oferta.producto.pk})
    return HttpResponseRedirect(detalle_producto_url)

def confirmar_recibido(request, oferta_id):
    oferta = get_object_or_404(OfertaDeEntrega, id=oferta_id)
    oferta.estado = 'entregado'
    oferta.save()
    producto = oferta.producto
    producto.estado = 'completado'  
    producto.save()

    detalle_producto_url = reverse('Detalle_producto', kwargs={'pk': oferta.producto.pk})
    return HttpResponseRedirect(detalle_producto_url)
