# passport/views.py
from django.shortcuts import render, redirect
from .models import Passport
from django.contrib.auth.models import User

def passport_create(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passport_number = request.POST.get("passport_number")
        issue_date = request.POST.get("issue_date")
        expiry_date = request.POST.get("expiry_date")
        birth_place = request.POST.get("birth_place")
        nationality = request.POST.get("nationality")

        user, created = User.objects.get_or_create(username=username)
        Passport.objects.create(
            user=user,
            passport_number=passport_number,
            issue_date=issue_date,
            expiry_date=expiry_date,
            birth_place=birth_place,
            nationality=nationality
        )
        return redirect("passport_list")
    return render(request, "passport/passport_form.html")

def passport_list(request):
    passports = Passport.objects.all()
    return render(request, "passport/passport_list.html", {"passports": passports})
