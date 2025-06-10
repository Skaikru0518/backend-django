from django.shortcuts import redirect, render
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image
from django.core.files.storage import FileSystemStorage

# Create your views here.
#@login_required
def home_page(request):
  images = Image.objects.all().order_by("-uploaded")
  context = {"images": images}
  return render(request, "index.html", context=context)

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
    
def upload(request):
  if request.method == "POST" and request.FILES["imageURL"]:
    _title = request.POST["title"]
    _image = request.FILES["imageURL"]
    fs = FileSystemStorage()
    _imageFile = fs.save(_image.name, _image)
    _user = request.user
    _private = "private" in request.POST
    newImage = Image(title = _title, imageURL = _imageFile, user = _user, private = _private)
    newImage.save()
    return redirect('/')
  
def setprivate(request):
  if request.method == "POST":
    currentId = request.POST["current"]
    currentImage = Image.objects.get(pk=currentId)
    currentImage.private = not currentImage.private
    currentImage.save()
    return redirect("/")