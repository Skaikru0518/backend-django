from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
#@login_required
def home_page(request):
  return render(request, "index.html")

def login_page(request):
  loginform = forms.LoginForm()
  message = ""
  if request.method == "POST":
    loginform = forms.LoginForm(request.POST)
    if loginform.is_valid():
      user = authenticate(
        username = loginform.cleaned_data["username"],
        password = loginform.cleaned_data["password"]
      )
      if user is not None:
        login(request, user) # request + user akit be akarunk jelentkeztetni
        return redirect("/")
      else:
        message = "Login failed!"
  context = {
    "loginform": loginform,
      "message": message
    }
  return render(request, "login.html", context=context)

def logout_page(request):
  logout(request)
  return redirect("/")

def register_page(request):
  registerfrom = forms.RegisterForm()
  context = {"registerform": registerfrom}
  return render(request, "register.html", context=context)

def register_user(request):
  if request.method == "POST":
    registerform = forms.RegisterForm(request.POST)
    if registerform.is_valid():
      username = registerform.cleaned_data["username"]
      password = registerform.cleaned_data["password"]
      first_name = registerform.cleaned_data["first_name"]
      last_name = registerform.cleaned_data["last_name"]
      email = registerform.cleaned_data["email"]
      newUser = User(username=username, first_name=first_name, last_name=last_name, email=email)
      newUser.set_password(password)
      newUser.save()
      return redirect("/")