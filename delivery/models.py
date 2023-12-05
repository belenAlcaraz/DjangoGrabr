from django.db import models
from accounts.models import Comprador,Viajero,Ubicacion 
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace_compra = models.URLField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.ImageField(upload_to='productos/',blank=True,null=True)
    recompensa = models.DecimalField(max_digits=10,decimal_places=2)
    usuario = models.ForeignKey(Comprador,on_delete=models.CASCADE)
    ubicacion_compra = models.ForeignKey(Ubicacion,related_name='ubicacion_compra', on_delete=models.CASCADE, blank=True, null=True)
    ubicacion_entrega = models.ForeignKey(Ubicacion,related_name='ubicacion_entrega', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('en proceso', 'En Proceso'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente')
    
    def __str__(self):
        return self.nombre
    
class OfertaDeEntrega(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    viajero = models.ForeignKey(Viajero,on_delete=models.CASCADE)
    precio_entrega = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_entrega_estimada = models.DateField()
    estado = models.CharField(max_length=50,choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente')

    def __str__(self) :
        return f"Oferta {self.producto.nombre} | {self.viajero.usuario.username}"