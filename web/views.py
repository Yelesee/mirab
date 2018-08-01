# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from google.cloud import translate

from .models import Student, Mark, Study, SysMark, PracLevel, Question, Practice

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

#from .forms import Calculate
#from fuzzy import fuzzy
from fuzzy import *

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

@csrf_exempt
def log_in(request):

    if ('dologin' in request.POST):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('your account is disabled')
        else:
                context = {'message': 'نام کاربری یا کلمه عبور اشتباه بود'}
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def log_out(request):
    if not request.user.is_anonymous:
        logout(request)
    return redirect('/')

@csrf_exempt
def recognize(request):
    return render(request, 'recognize.html')  

@csrf_exempt
def define(request): 
    inputs = int(request.POST.get('inputs'))
    outputs = int(request.POST.get('outputs'))
    rules = int(request.POST.get('rules'))

    context = {'inputs':inputs, 'outputs':outputs, 'rules':rules}
    return render(request, 'define.html', context) 