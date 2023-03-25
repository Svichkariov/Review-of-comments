from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import login, home, Reg, LoginUser

from django.contrib.auth.forms import AuthenticationForm




urlpatterns = [
    path('', LoginUser.as_view()),
    path('reg/', Reg.as_view()),
    path('home/', home, name='home'),


]
