# gestion_imei/models.py
from django.db import models

class Cell(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    imei = models.CharField(max_length=15, unique=True)
    vendido = models.BooleanField(default=False)
    comprador = models.CharField(max_length=100, blank=True, null=True)
    robado = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.imei})'
