from django import forms
from .models import Producto, OfertaDeEntrega

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'enlace_compra', 'precio', 'imagen', 'recompensa', 'ubicacion_compra', 'ubicacion_entrega']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'enlace_compra': forms.URLInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'recompensa': forms.NumberInput(attrs={'class': 'form-control'}),
            'ubicacion_compra': forms.Select(attrs={'class': 'form-control'}),
            'ubicacion_entrega': forms.Select(attrs={'class': 'form-control'}),
        }


class OfertaDeEntregaForm(forms.ModelForm):
    class Meta:
        model = OfertaDeEntrega
        fields = ['viajero', 'precio_entrega', 'fecha_entrega_estimada']
        widgets = {
        'viajero': forms.Select(attrs={'class': 'form-control'}),
        'precio_entrega': forms.NumberInput(attrs={'class': 'form-control'}),
        'fecha_entrega_estimada': forms.NumberInput(attrs={'type':'date', 'class': 'form-control','placeholder': 'dd/mm/aaaa'}),
    }