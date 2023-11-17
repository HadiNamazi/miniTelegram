from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.contrib.auth.forms import UserCreationForm

@login_required() #TODO
def home(req):
    contacts = req.user.contacts
    print(contacts)

def sign_up(req):
    if not req.user.is_authenticated:
        form = forms.UserRegistration
        if req.method == 'GET':
            context = {'form': form}
            return render(req, 'base/signup.html', context)