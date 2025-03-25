from django.urls import path
from . import views

app_name = "weather"
urlpatterns = [
  path('', views.indexPage, name="indexPage"),
  path("addpage/", views.addPage, name="addPage"),
  #ide kell beirni a backend api-kat is
  path("addmeasure/", views.addMeasure, name="addMeasure"),
  path("delete/<int:measureid>", views.deleteMeasure, name="deleteMeasure"),
]