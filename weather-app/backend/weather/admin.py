from django.contrib import admin

# importaljuk a modelleinket
from .models import City, WeatherData

# Register your models here.
admin.site.register(City)
admin.site.register(WeatherData)


