from django.forms import ModelForm
from django import forms
from . import models

class UserRegistration(ModelForm):
    passconfirm = forms.CharField(max_length=50)

    class Meta:
        model = models.User
        fields = ['username', 'userId', 'password', 'passconfirm']

        # doesn't work
        labels = {
            "passconfirm":  "password confirmation",
        }
