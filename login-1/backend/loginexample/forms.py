from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(max_length=64)
  password = forms.CharField(max_length=64, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
  username = forms.CharField(max_length=64)
  password = forms.CharField(max_length=64, widget=forms.PasswordInput)
  first_name = forms.CharField(max_length=64)
  last_name = forms.CharField(max_length=64) #lehet required=True -> muszaj megadni
  email = forms.EmailField()