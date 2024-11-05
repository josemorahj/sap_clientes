from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    nro_calle = models.IntegerField()
    pais = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'domicilio {self.id}: {self.calle} {self.nro_calle} {self.pais}'

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f'persona {self.id}: {self.nombre} {self.apellido} {self.email}'