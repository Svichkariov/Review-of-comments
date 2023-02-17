from django.urls import path


from .views import *

urlpatterns = [
    path('', login),
    path('home/', home),
    # path('search_for_comments/', search_for_comments),
    # path('organization/', organization),
]