from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

# VIEW
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View, TemplateView, DeleteView

# Authentication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms
from django.contrib.auth.forms import AuthenticationForm

# models
from django.contrib.auth.models import User

# message
from django.contrib import messages

import uuid
from django.db.models import Q

from e_app.EmailBackEnd import EmailBackEnd
#######################################################################
#######################################################################


def REGISTER(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'User Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, "Email Already Exists")
                return redirect('register')
            else:
                obj = User.objects.create_user(
                    username=username, email=email, password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User Create Succefully')
                return redirect('login')
        else:
            messages.warning(request, "password doesn't match")
            return redirect('register')
    return render(request, 'registration/register.html')

def DO_LOGIN(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackEnd.authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Email or password.')
            return redirect('login')