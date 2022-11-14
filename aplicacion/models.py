from email.policy import default
from tabnanny import verbose
from django.db import models

class Persona(models.Model):
    primerNombre = models.CharField(max_length=50, verbose_name='Primer Nombre')
    segundoNombre = models.CharField(max_length=50, verbose_name='Segundo Nombre')
    primerApellido = models.CharField(max_length=50, verbose_name='Primer Apellido')
    segundoApellido = models.CharField(max_length=50, verbose_name='Segundo Nombre')
    edad = models.IntegerField(default=0, verbose_name='Edad')
    correo = models.EmailField(max_length=50, verbose_name='Correo')
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña')

    def __str__(self):
        return self.correo, self.contrasena

