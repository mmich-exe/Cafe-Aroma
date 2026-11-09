from django.db import models
from django.core.validators import MinValueValidator

class TipoCafe(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cafe(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.ForeignKey(TipoCafe, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    disponible = models.BooleanField(default=True)
    fecha_incorporacion = models.DateField()

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"