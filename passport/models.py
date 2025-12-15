from django.db import models
from django.contrib.auth.models import User

class Passport(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    birth_place = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} — {self.passport_number}"
