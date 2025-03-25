from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import City, WeatherData

# Create your views here.
@csrf_protect
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

def addMeasure(request):
 if request.method == "POST":
  _cityId = request.POST["city"]
  _city = None
  if _cityId == "addNew":
    _newCity = request.POST["newCity"]
    newCity = City(cityName = _newCity, capital = False)
    newCity.save()
    _city = newCity
  else:
    _city = City.objects.get(pk=_cityId)
  _temp = request.POST["temp"]
  _rain = request.POST["rain"]
  _location = request.POST["location"]

  #peldanyositunk es megadjuk a class ertekeit, hogy mi mit kapjon postolasnal
  newWeather = WeatherData(city = _city, temperature = _temp, rainfall = _rain, location = _location)
  newWeather.save() #adatbazisba kuldes
  return redirect("/")


def deleteMeasure(requrest, measureid):
  if requrest.method == "POST":
    current = WeatherData.objects.get(pk = measureid)
    current.delete()
  return redirect('/')