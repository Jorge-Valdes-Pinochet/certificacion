from django.db import models
from django.contrib.auth.models import User

class Terminal(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Anden(models.Model):
    estado = models.CharField(max_length=20, choices=[
        ('ocupado', 'Ocupado'),
        ('disponible', 'Disponible'),
        ('mantencion', 'Mantención')
    ])
    terminal = models.ForeignKey(Terminal, on_delete=models.CASCADE)

    def __str__(self):
        return f"Andén {self.id} - {self.terminal.nombre}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Bus(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    estacionado = models.ForeignKey(Anden, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.patente

class BusEstacionado(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    llegada = models.DateTimeField(auto_now_add=True)
    salida = models.DateTimeField(null=True, blank=True)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Bus {self.bus.patente} - {self.llegada}"