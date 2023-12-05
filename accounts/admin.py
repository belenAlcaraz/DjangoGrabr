from django.contrib import admin
from .models import User, Comprador,Viajero, Ubicacion

admin.site.register(Ubicacion)
admin.site.register(User)
admin.site.register(Comprador)
admin.site.register(Viajero)

