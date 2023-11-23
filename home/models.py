from django.db import models
from django.contrib.auth.models import User

# Create your models here.
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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
