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
from e_app.models import Categories,Course, Author

# message
from django.contrib import messages

import uuid
from django.db.models import Q

#######################################################################
#######################################################################


def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    catagories = Categories.objects.all().order_by('-id')[0:5]
    courses = Course.objects.filter(status='PUBLISH').order_by('-id')

    context = {
        'category':catagories,
        'course':courses
    }
    return render(request, 'main/home.html',context)


def SINGLE_COURSE(request):
    return render(request, 'main/single_course.html')


def CONTACT_US(request):
    return render(request, 'main/contac_us.html')


def ABOUT_US(request):
    return render(request, 'main/about.html')
