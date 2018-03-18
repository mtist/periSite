from django import forms
from.models import People


class RegisterForm(forms.ModelForm):
    class Meta:
        model = People
        exclude = ['']
