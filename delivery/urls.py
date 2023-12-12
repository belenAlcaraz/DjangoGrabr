from delivery.views import InicioView
from django.urls import path
from .views import ComprarProductoView, DetalleProductoView, ListaProductosView, OfertaView

urlpatterns = [
    path('', InicioView.as_view(), name='Inicio'),
    path('compra/', ComprarProductoView.as_view(), name='Compra'),
    path('detalle_producto/<int:pk>/', DetalleProductoView.as_view(), name='Detalle_producto'),
    path('listado_productos/', ListaProductosView.as_view(), name='Lista_producto'),
    path('hacer_oferta_entrega/<int:pk>/', OfertaView.as_view(), name='Oferta_entrega'),
]