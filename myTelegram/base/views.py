from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def home(req):
    # contacts = req.user.contacts
    # print(contacts)
    context = {}
    return render(req, 'base/home.html', context)

def sign_up(req):
    print(req.user)
    if req.user.is_authenticated:
        messages.error(req, "you're logged in already")
        return redirect('home')

    if req.method == 'POST':
        form = forms.UserRegistration(req.POST)
        if form.is_valid():
            if req.POST['password'] == req.POST['passconfirm']:
                user = form.save()
                login(req, user)
                return redirect('home')
            else:
                messages.error(req, 'please enter password carefully')

    form = forms.UserRegistration
    context = {'form': form}
    return render(req, 'base/signup.html', context)
