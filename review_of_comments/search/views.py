from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


# class DataMixin:
#     def get_user_context(self, **kwargs):
#         context = kwargs




class Reg(CreateView):
    form_class = UserCreationForm
    template_name = 'reg.html'
    success_url = reverse_lazy('login.html')

    # def get_context_data(self,*, object_list=None,  **kwargs):
    #     context = super().get_context_data()
    #     c_def = self.get_user_context(title='registr')
    #     return (list(context.items() + list(c_def.items()) ))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    # def get_success_url(self):
    #     return reverse_lazy('home')


def home(request):
    return render(request, 'home.html')

