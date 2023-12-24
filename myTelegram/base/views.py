from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# checks if contacts are repeated, returns True; otherwise returns False
def contacts_repeatation(contacts):
    if contacts is None:
        return False
    contacts_list = contacts.split(' ')
    contacts_list = contacts_list[:-1]
    seen = []
    for contact in contacts_list:
        if not contact in seen:
            seen.append(contact)
        else:
            return True
    return False

# lists User object of contact IDs
def contacts_exporter(contacts):
    contacts_list = contacts.split(' ')
    contacts_list = contacts_list[:-1]
    output = []
    for contact in contacts_list:
        try:
            c = models.User.objects.get(userId=contact)
        except:
            return 
        output.append(c)
    return output

def id_validation(id):
    try:
        models.User.objects.get(userId=id)
        return True
    except:
        return False

def home(req):
    if req.user.is_authenticated:

        me = models.User.objects.get(userId=req.user.userId)

        # POST method
        if req.method == 'POST':

            # contact search posted
            try:
                contact_id = req.POST['add_contact']

                # adding contact to user contacts
                if me.contacts is not None:
                    temp_contacts = me.contacts + contact_id + ' '
                else:
                    temp_contacts = contact_id + ' '

                # if user contacts was valid, save it
                if not contacts_repeatation(temp_contacts) and id_validation(contact_id):
                    me.contacts = temp_contacts
                    me.save()

                return redirect('home')

            # sth else posted
            except:
                return redirect('home')


        # GET method

        # making contacts list
        if me.contacts is not None:
            contacts = contacts_exporter(me.contacts)
        else:
            contacts = []

        context = {'contacts': contacts}
        return render(req, 'base/home.html', context)
    
    # if not logged in, redirect to signup page
    return redirect('signup')

def sign_up(req):
    # check if user signed up already or not
    if req.user.is_authenticated:
        messages.error(req, "you're logged in already")
        return redirect('home')

    if req.method == 'POST':

        username = req.POST['username']
        password = req.POST['password']
        passconfirm = req.POST['passconfirm']
        id = req.POST['userId']
        form = forms.UserRegistration(username=username, password=password, passconfirm=passconfirm, id=id)

        try:
            remember_me = req.POST['remember_me']
        except:
            remember_me = 'off'

        # validation
        if form.is_valid() and not ' ' in id:
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

def pv(req, id):

    context = {}
    return render(req, 'base/pv.html', context)