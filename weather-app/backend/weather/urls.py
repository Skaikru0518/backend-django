from django.urls import path
from . import views

app_name = "weather"
urlpatterns = [
  path('', views.indexPage, name="indexPage"),
  path("addpage/", views.addPage, name="addPage")
]