from django.urls import path
from .views import PassportCreateView, PassportListView

urlpatterns = [
    path("", PassportListView.as_view(), name="passport_list"),
    path("create/", PassportCreateView.as_view(), name="passport_create"),
]

