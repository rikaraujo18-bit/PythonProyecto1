from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre
