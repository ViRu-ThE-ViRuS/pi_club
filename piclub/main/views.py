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

def videos_page(request):
    return render(request, 'main/videos.html')

def quiz_page(request):
    return render(request, 'main/quiz.html')

def list_of_quiz(request):
    return render(request, 'main/list_of_quiz.html')

def great_people(request):
    return render(request, 'main/great_people.html')

def facts(request):
    return render(request, 'main/facts.html')
