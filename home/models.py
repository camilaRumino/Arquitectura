from django.db import models

# Create your models here.
class Usuario(models.Model):
    run = models.CharField(max_length=12)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.CharField(max_length=50) 
    contrasena = models.CharField(max_length=20)
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
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    taller = models.ForeignKey(Taller, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    
