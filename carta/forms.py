from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['codigo', 
                  'nombre', 
                  'descripcion', 
                  'tipo', 
                  'precio', 
                  'stock', 
                  'disponible', 
                  'fecha_incorporacion']
        widgets = {
            'fecha_incorporacion': forms.DateInput(attrs={'type': 'date'}),
        }