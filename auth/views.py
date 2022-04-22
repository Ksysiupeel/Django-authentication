from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request: HttpRequest):
    return render(request, "index.html")

def register(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user")
    else:
        form = RegisterForm()
    
    return render(request, "registration/sign_up.html", {"form": form})

@login_required(login_url="/login")
def user(request: HttpRequest):
    return render(request, "user.html")