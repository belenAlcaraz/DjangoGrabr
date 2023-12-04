from django.db import models
from cities_light.models import Country,City
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Ubicacion(models.model):
    pais = models.ForeignKey(Country, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.ciudad.name}, {self.pais.name}"
    
class User(AbstractUser):
    es_comprador= models.BooleanField(default=False)
    es_viajero= models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Comprador(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, related_name='comprador')
    foto_perfil = models.ImageField(upload_to='compradores/', blank=True, null=True)
    ubicacion_actual= models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username

class Viajero(models.Modelodel):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, related_name='viajero')
    foto_perfil =  models.ImageField(upload_to='viajeros/', blank=True, null=True)
    ubicacion_actual =  models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    ubicacion_regreso = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    en_viaje = models.BooleanField(False)

    def __str__(self):
        return self.usuario.username

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace_compra = models.URLField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    imagen = models.ImageField(upload_to='productos/',blank=True,null=True)
    recompensa = models.DecimalField(max_digits=10,decimal_places=2)
    usuario = models.ForeignKey(Comprador,on_delete=models.CASCADE)
    ubicacion_compra = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True, null=True)
    ubicacion_entrega = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=[('pendiente', 'Pendiente'), ('en proceso', 'En Proceso'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente')
    
    def __str__(self):
        return self.nombre
    
class OfertaDeEntrega(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    viajero = models.ForeignKey(Viajero,on_delete=models.CASCADE)
    precio_entrega = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_entrega_estimada = models.DecimalField()
    estado = models.CharField(max_length=50,choices=[('pendiente', 'Pendiente'), ('aceptado', 'Aceptado'), ('entregado', 'Entregado'), ('cancelado', 'Cancelado')], default='pendiente')

    def __str__(self) :
        return f"Oferta {self.producto.nombre} | {self.viajero.usuario.username}"