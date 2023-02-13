from django.urls import path

from .views import *

urlpatterns = [
    path('', home),
    path('account/', account),
    path('search_for_comments/', search_for_comments),
    path('organization/', organization),
]