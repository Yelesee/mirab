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

from .forms import SignUpForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

#from .forms import Calculate
#from fuzzy import fuzzy
from fuzzy import *
from lists import *
def home(request):
    return render(request, 'home.html')

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

@login_required
@csrf_exempt
def form(request):
    return render(request, 'form.html')

@login_required
@csrf_exempt
def response(request):
    all = request.POST
    data = dict(all)
    context = {'data':data}
    return render(request, 'response.html', context) 