# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# redirect to main page
def index(request):
    return render(request, 'main/home.html')

# redirect to login page
def login(request):
    return render(request, 'main/login.html')

# redirect to sign up page
def sign_up(request):
    return render(request, 'main/sign_up.html')

# redirect to about page
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')