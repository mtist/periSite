from django import forms
from.models import People


class RegisterForm(forms.ModelForm):
    # cafe = forms.IntegerField(max_value=100)

    class Meta:
        model = People
        exclude = ['']
