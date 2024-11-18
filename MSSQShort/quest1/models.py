from django.db import models

class quest1(models.Model):
    idade = models.IntegerField()
    sexo = models.FloatField(null=True, blank=True)
    nao_aplicavel =  models.FloatField(null=True, blank=True)
    nunca = models.FloatField(null=True, blank=True)
    raramente = models.FloatField(null=True, blank=True)
    algumas_vezes = models.FloatField(null=True, blank=True)
    frequentemente = models.FloatField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
 
