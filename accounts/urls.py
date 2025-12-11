from django.urls import path
from .views import register_view, login_view, all_people

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("people/", all_people, name="all_people"),
]
