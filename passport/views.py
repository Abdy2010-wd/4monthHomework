from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .models import Passport


class PassportCreateView(CreateView):
    model = Passport
    fields = [
        "passport_number",
        "issue_date",
        "expiry_date",
        "birth_place",
        "nationality",
    ]
    template_name = "passport/passport_form.html"
    success_url = reverse_lazy("passport_list")

    def form_valid(self, form):
        username = self.request.POST.get("username")
        user, created = User.objects.get_or_create(username=username)
        form.instance.user = user
        return super().form_valid(form)


class PassportListView(ListView):
    model = Passport
    template_name = "passport/passport_list.html"
    context_object_name = "passports"
