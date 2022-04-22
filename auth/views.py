from django.shortcuts import render
from django.http import HttpRequest
from .forms import RegisterForm

# Create your views here.
def home(request: HttpRequest):
    return render(request, "index.html")

def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    
    return render(request, "registration/sign_up.html", {"form": form})