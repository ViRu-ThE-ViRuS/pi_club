# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/home.html')

def login(request):
    return render(request, 'main/login.html')

def sign_up(request):
    return render(request, 'main/sign_up.html')