from django.forms import ModelForm
from django import forms
from . import models

class UserRegistration(ModelForm):
    passconfirm = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Password confirmation'}))
    remember_me = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = models.User
        fields = ['username', 'userId', 'password', 'passconfirm', 'remember_me']

class UserLogin(ModelForm):
    remember_me = forms.BooleanField(required=False, initial=True)

    class Meta:
        model = models.User
        fields = ['userId', 'password', 'remember_me']

class message(ModelForm):
    class Meta:
        model = models.Message
        fields = ['text']