from django.forms.models import BaseModelForm
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView, DetailView
from .models import Producto, OfertaDeEntrega
from accounts.models import Comprador
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

    def form_valid(self, form: BaseModelForm):
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

class OfertaView(CreateView):
    model =  OfertaDeEntrega
    form_class = OfertaDeEntregaForm
    template_name = 'hacer_oferta_entrega.html'

def crear_oferta(request, producto_id):
        producto = Producto.objects.get(pk=producto_id)

        if request.method == 'POST':
            form = OfertaDeEntregaForm(request.POST)
            if form.is_valid():
                oferta = form.save(commit=False)
                oferta.producto = producto
                oferta.viajero = request.user 
                oferta.save()           

                producto.estado = 'en proceso'
                producto.save()

                return redirect('detalle_producto', producto_id=producto_id)
        else:
            form = OfertaDeEntregaForm()

        return render(request, 'Inicio', {'form': form, 'producto': producto})