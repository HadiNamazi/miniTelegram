from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def home(req):
    if req.user.is_authenticated:
        context = {}
        return render(req, 'base/home.html', context)
    
    # if not logged in, redirect to signup page
    return redirect('signup')

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

    # GET method
    form = forms.UserRegistration
    context = {'form': form}
    return render(req, 'base/signup.html', context)

def login_page(req):
    if req.user.is_authenticated:
        messages.error(req, "You're already logged in.")
        return redirect('home')
    
    if req.method == 'POST':
        form = forms.UserLogin(req.POST)
        userId = req.POST['userId']
        password = req.POST['password']
        try:
            remember_me = req.POST['remember_me']
        except:
            remember_me = 'off'

        try:
            user = models.User.objects.get(userId=userId)
        except:
            # userId is invalid
            messages.error(req, 'Your Id is invalid. try again!')
            return redirect('login_page')
        
        if user.password == password:
            # everything is ok and logging in
            login(req, user)

            # remember me checkbox
            if remember_me == 'off':
                    req.session.set_expiry(0)

            return redirect('home')

        # password is incorrect
        messages.error(req, 'Your password is incorrect. try again!')
        return redirect('login_page')


    # GET method
    form = forms.UserLogin()
    context = {'form': form}
    return render(req, 'base/login.html', context)

def logout_user(req):
    logout(req)
    return redirect('home')
