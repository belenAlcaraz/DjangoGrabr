from delivery.views import InicioView
from django.urls import path
from .views import ComprarProductoView, DetalleProductoView, ListaProductosView, OfertaView,OfertasViajeroView,PedidosViajeroView, CompraDetalleViajero, aceptar_oferta, rechazar_oferta, confirmar_recibido 

urlpatterns = [
    path('', InicioView.as_view(), name='Inicio'),
    path('compra/', ComprarProductoView.as_view(), name='Compra'),
    path('detalle_producto/<int:pk>/', DetalleProductoView.as_view(), name='Detalle_producto'),
    path('listado_productos/', ListaProductosView.as_view(), name='Lista_producto'),
    path('hacer_oferta_entrega/<int:pk>/', OfertaView.as_view(), name='Oferta_entrega'),
    path('ofertas_viajero/', OfertasViajeroView.as_view(), name='Ofertas_viajero'),
    path('pedidos/viajero/', PedidosViajeroView.as_view(), name='Pedidos_viajero'),
    path('compra_detalle_viajero/<int:pk>/', CompraDetalleViajero.as_view(), name='Compra_detalle_viajero'),
    path('aceptar_oferta/<int:oferta_id>/', aceptar_oferta, name='Aceptar_oferta'),
    path('rechazar_oferta/<int:oferta_id>/', rechazar_oferta, name='Rechazar_oferta'),
    path('confirmar_recibido/<int:oferta_id>/', confirmar_recibido, name='Confirmar_recibido'),
]