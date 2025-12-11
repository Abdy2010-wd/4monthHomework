from django import forms
from captcha.fields import CaptchaField
from .models import Application

class ApplicationForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Application
        fields = [
            "full_name", "email", "phone", "age", "city",
            "address", "education", "experience",
            "skills", "desired_position"
        ]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


        