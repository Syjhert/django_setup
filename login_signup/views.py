from django.shortcuts import render
from .forms import LoginForm, SignupForm

# Create your views here.
def gateway_view(request):
    return render(request, 'gateway.html')

def login_view(request):
    print("View called")
    if request.method == "POST":
        form = LoginForm(request.POST)
        print("Post request")
        if form.is_valid():
            print("Form is valid")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request, 'home.html', {'username': username})
    else:
        form = LoginForm()
    print("Rendering")
    return render(request, 'login.html', {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            gender = form.cleaned_data['gender']
            return render(request, 'home.html', {'username': username})
    else:
        form = SignupForm()
    return render(request, 'signup.html', {"form": form})