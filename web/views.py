# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from google.cloud import translate
# import json

from .models import Student
from .forms import SignUpForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

#from .forms import Calculate
#from fuzzy import fuzzy
from fuzzy import *
from lists import *
def home(request):
    return render(request, 'home.html')
    
def index(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')
    else:
       context = {}
       return render(request, 'index.html', context)

########################################################################
@csrf_exempt
def json(request):
    context = {}
    return render(request, 'json.html', context)
########################################################################

@csrf_exempt
def check(request):
    context = {}
    return render(request, 'check.html', context)

@csrf_exempt
def calculate(request):
    
    mark = float(request.POST['mark'])
    study = float(request.POST['study'])
    hardness = float(request.POST['hardness'])
    sysmark = float(request.POST['sysmark'])

    x = FuzzyLogic(mark,study,hardness,sysmark)
    x.fuzzification()
    a = x.rulebase()
    resault = x.defuzzification(a)

    return render(request, 'check.html', {'resault': resault,})

# @csrf_exempt
# def login(request):
#     if ('dologin' in request.POST):
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 return HttpResponse('your account is disabled')
#         else:
#                 context = {'message': 'نام کاربری یا کلمه عبور اشتباه بود'}
#                 return render(request, 'login.html', context)
#     else:
#         return render(request, 'login.html')

# def logout(request):
#     if not request.user.is_anonymous:
#         logout(request)
#     return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email_address = form.cleaned_data.get('email_address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password, email=user.profile.email_address)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def form(request):
    return render(request, 'form.html') 

@csrf_exempt
def response(request):
    all = request.POST
    data = dict(all)
    context = {'data':data}
    return render(request, 'response.html', context) 