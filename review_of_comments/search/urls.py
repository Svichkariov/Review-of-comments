from django.urls import path

from .views import home, setup

urlpatterns = [
    path('', home, name='home'),
    path('home/setup/', setup, name='setup')
]
