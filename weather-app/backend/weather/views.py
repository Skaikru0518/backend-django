from django.shortcuts import render
from .models import City, WeatherData

# Create your views here.

def indexPage(request):
  #lekerdezzuk a mereseket: select * from weatherData orderby measuretime desc
  allDatas = WeatherData.objects.all().order_by("-measureTime")
  context={"data": allDatas} # templatenél a datara hivatkozunk
  return render(request, "index.html", context) 
  # megadjuk hogy melyik html-t rendelerelje le, és mi legyen a contentje->context

def addPage(request):
  allCities = City.objects.all().order_by('cityName')
  context = {"cities": allCities}
  return render(request, "add.html", context)

