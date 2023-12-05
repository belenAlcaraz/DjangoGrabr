from django.db import models
from cities_light.models import Country,City
from django.contrib.auth.models import AbstractUser


class Ubicacion(models.Model):
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

class Viajero(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE, related_name='viajero')
    foto_perfil =  models.ImageField(upload_to='viajeros/', blank=True, null=True)
    ubicacion_actual =  models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    ubicacion_regreso = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    en_viaje = models.BooleanField(False)

    def __str__(self):
        return self.usuario.username