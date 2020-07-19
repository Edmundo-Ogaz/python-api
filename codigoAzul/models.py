from django.db import models

class Albergue(models.Model):
    region = models.CharField(max_length=100, blank=True, default='')
    tipo = models.CharField(max_length=100, blank=True, default='')
    comuna = models.CharField(max_length=100, blank=True, default='')
    nombre = models.CharField(max_length=100, blank=True, default='')
    direccion = models.CharField(max_length=100, blank=True, default='')
    institucion = models.CharField(max_length=100, blank=True, default='')
    horario = models.CharField(max_length=100, blank=True, default='')
    cupo = models.CharField(max_length=100, blank=True, default='')
    mapa = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['region']
