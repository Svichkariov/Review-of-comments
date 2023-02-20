from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy

# from review_of_comments.search.forms import RegisterUserForm


def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def search_settings(request):
    return render(request, 'search-settings.html')

def home(request):
    return render(request, 'base.html')

#
# def search_for_comments(request):
#     return render(request, 'login.html')
#
# def organization(request):
#     return HttpResponse('Организация')


