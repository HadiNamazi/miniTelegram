from django.forms import ModelForm, PasswordInput
from . import models

class UserRegistration(ModelForm):
    passconfirm = PasswordInput()

    class Meta:
        model = models.User
        fields = ['name', 'email', 'password', 'passconfirm']

    # def clean(self):
