from django.db import models

class Familiares(models.Model): 

    nombre = models.CharField(max_length=50) 
    numero_tel = models.IntegerField()
    fecha_nac = models.CharField(max_length=50)
