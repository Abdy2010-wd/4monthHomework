from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "body", "book"]

    book = forms.IntegerField(widget=forms.HiddenInput())
