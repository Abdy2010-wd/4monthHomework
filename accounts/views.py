from django.views.generic import CreateView, FormView, ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import ApplicationForm, LoginForm
from .models import Application


class RegisterView(CreateView):
    form_class = ApplicationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("all_people")

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        if user:
            login(self.request, user)
        return super().form_valid(form)


class AllPeopleView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "accounts/people.html"
    context_object_name = "people"
