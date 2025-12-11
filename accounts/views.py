from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import ApplicationForm, LoginForm
from .models import Application


def register_view(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = ApplicationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user:
                login(request, user)
                return redirect("all_people")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


@login_required
def all_people(request):
    people = Application.objects.all()
    return render(request, "accounts/people.html", {"people": people})

