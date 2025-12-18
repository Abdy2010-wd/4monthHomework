from django.urls import path
from .views import RegisterView, LoginView, AllPeopleView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("people/", AllPeopleView.as_view(), name="all_people"),
]

