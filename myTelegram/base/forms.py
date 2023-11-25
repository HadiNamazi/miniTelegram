from django.forms import ModelForm
from django import forms
from . import models

class UserRegistration(ModelForm):
    passconfirm = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Password confirmation'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['userId'].widget.attrs['placeholder'] = 'Id'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

    class Meta:
        model = models.User
        fields = ['username', 'userId', 'password', 'passconfirm']

        # doesn't work
        labels = {
            "passconfirm":  "password confirmation",
        }
