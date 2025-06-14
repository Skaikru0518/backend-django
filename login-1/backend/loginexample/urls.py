from django.urls import path
from . import views

app_name="loginexample"
urlpatterns = [
  path('', views.home_page, name="home"),
  path('login', views.login_page, name="login"),
  path('logout', views.logout_page, name="logout"),
  path('register', views.register_page, name="register"),
  path('registeruser', views.register_user, name="registeruser"),
  path("upload", views.upload, name="upload"),
  path("setprivate", views.setprivate, name="setprivate")
]
