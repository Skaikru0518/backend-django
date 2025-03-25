from django.db import models
from django.utils.timezone import now

# Create your models here.

class City(models.Model):
  cityName = models.CharField(max_length=200)
  capital = models.BooleanField() # capital or not

  def __str__(self):
    return self.cityName
  
  class Meta:
     verbose_name_plural = 'cities' # nem citys, hanem felulbiraljuk, hogy cities legyen az admin feluleten a nev
  
class WeatherData(models.Model):
  city = models.ForeignKey("City", on_delete=models.CASCADE) # City--> a masik modell(class) neve, mert o a foreign key
  temperature = models.FloatField()
  rainfall = models.IntegerField()
  measureTime = models.DateTimeField(default=now)
  location = models.CharField(max_length=150)
  

  def __str__(self): # ez jelöli, hogy az admin felületen mit lássunk belőle
      return f"{self.location} ({self.measureTime})"
  
