from django.db import models


class banco_quest1(models.Model):
    idade = models.IntegerField()
    sexo = models.IntegerField(null=True, blank=True)
    carros = models.IntegerField(null=True, blank=True)
    autocarros = models.IntegerField(null=True, blank=True)
    comboios = models.IntegerField(null=True, blank=True)
    avioes = models.IntegerField(null=True, blank=True)
    embarcacao_pequena = models.IntegerField(null=True, blank=True)
    navios = models.IntegerField(null=True, blank=True)
    baloicos = models.IntegerField(null=True, blank=True)
    carroseis = models.IntegerField(null=True, blank=True)
    montanha_russa = models.IntegerField(null=True, blank=True)

    carros2 = models.IntegerField(null=True, blank=True)
    autocarros2 = models.IntegerField(null=True, blank=True)
    comboios2 = models.IntegerField(null=True, blank=True)
    avioes2 = models.IntegerField(null=True, blank=True)
    embarcacao_pequena2 = models.IntegerField(null=True, blank=True)
    navios2 = models.IntegerField(null=True, blank=True)
    baloicos2 = models.IntegerField(null=True, blank=True)
    carroseis2 = models.IntegerField(null=True, blank=True)
    montanha_russa2 = models.IntegerField(null=True, blank=True)
