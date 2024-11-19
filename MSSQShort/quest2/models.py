from django.db import models


class banco_quest2(models.Model):
    altura = models.FloatField()
    cintura = models.FloatField()
    peso = models.FloatField()
    imc = models.FloatField()
    pressao = models.FloatField()
    oximetria = models.FloatField()
    frequencia_card = models.FloatField()
