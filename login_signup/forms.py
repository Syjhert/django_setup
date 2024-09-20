from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    gender = forms.CharField(label="Gender", max_length=20)