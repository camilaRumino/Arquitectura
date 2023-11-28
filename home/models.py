from django.contrib.auth.models import User
from django.db import models

class DetalleUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=12)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    fecnac = models.DateField()
   
    def __str__(self):
        return self.nombre

class Taller(models.Model):
    nombre = models.CharField(max_length=200)
    dia = models.CharField(max_length=50)
    hora = models.TimeField()
    instructor = models.CharField(max_length=100)
    sala = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="talleres", null=True)

    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
