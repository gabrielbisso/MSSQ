from django.db import models


class quest3(models.Model):
    nausea = models.FloatField(null=True, blank=True)
    vomito = models.FloatField(null=True, blank=True)
    tontura = models.FloatField(null=True, blank=True)
    suor = models.FloatField(null=True, blank=True)
    palidez = models.FloatField(null=True, blank=True)
    dorcab = models.FloatField(null=True, blank=True)
    cansaco = models.FloatField(null=True, blank=True)
    bocejo = models.FloatField(null=True, blank=True)
    hiperv = models.FloatField(null=True, blank=True)
    outros = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
