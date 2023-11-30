from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def home(req):
    context = {}
    return render(req, 'base/home.html', context)

def sign_up(req):
    # check if user signed up already or not
    if req.user.is_authenticated:
        messages.error(req, "you're logged in already")
        return redirect('home')

    if req.method == 'POST':

        form = forms.UserRegistration(req.POST)
        password = req.POST['password']
        passconfirm = req.POST['passconfirm']
        try:
            remember_me = req.POST['remember_me']
        except:
            remember_me = 'off'

        # validation
        if form.is_valid():
            if password == passconfirm:
                # registration
                user = form.save()
                # login after registration
                login(req, user)

                # remember me checkbox
                if remember_me == 'off':
                    req.session.set_expiry(0)

                return redirect('home')
            else:
                messages.error(req, 'please enter password carefully')

    form = forms.UserRegistration
    context = {'form': form}
    return render(req, 'base/signup.html', context)
