from django.urls import path
from . import views


urlpatterns = [
  path('bejelentesek', views.osszesBejelentes, name="osszesBejelentes"),
  path('bejelentes/<str:vnev>', views.varosBejelentes, name="varosBejelentes")
]
