from django.db import models


class banco_quest1(models.Model):
    idade = models.IntegerField()
    sexo = models.IntegerField(null=True, blank=True)
    carros = models.IntegerField(null=True, blank=True)
    autocarros = models.IntegerField(null=True, blank=True)
    comboios = models.IntegerField(null=True, blank=True)
    aviões = models.IntegerField(null=True, blank=True)
    embarcacao_pequena = models.IntegerField(null=True, blank=True)
    navios = models.IntegerField(null=True, blank=True)
    baloiços = models.IntegerField(null=True, blank=True)
    carroseis = models.IntegerField(null=True, blank=True)
    montanha_russa = models.IntegerField(null=True, blank=True)

    carros10 = models.IntegerField(null=True, blank=True)
    autocarros10 = models.IntegerField(null=True, blank=True)
    comboios10 = models.IntegerField(null=True, blank=True)
    aviões10 = models.IntegerField(null=True, blank=True)
    embarcacao_pequena10 = models.IntegerField(null=True, blank=True)
    navios10 = models.IntegerField(null=True, blank=True)
    baloiços10 = models.IntegerField(null=True, blank=True)
    carroseis10 = models.IntegerField(null=True, blank=True)
    montanha_russa10 = models.IntegerField(null=True, blank=True)
