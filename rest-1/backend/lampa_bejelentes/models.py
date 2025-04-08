from django.db import models
from django.utils.timezone import now

# Create your models here.

class Varos(models.Model):
  varosNev = models.CharField(max_length=200)

  def __str__(self):
    return self.varosNev
  
  class Meta:
     verbose_name_plural = "Varosok"

class Bejelentes(models.Model):
  varos = models.ForeignKey(Varos, on_delete=models.CASCADE)
  bejelento = models.CharField(max_length=200)
  utca = models.CharField(max_length=200)
  lampatestek = models.IntegerField()
  datum = models.DateTimeField(default=now)

  def __str__(self):
      return str(self.datum) + " - " + self.utca
  
  class Meta:
     verbose_name_plural = "Bejelentesek"