from django.urls import path


from .views import login, registration, home, search_settings

urlpatterns = [
    path('', login, name='login'),
    path('registration/', registration, name='registration'),
    path('home/', home),
    path('home/search_settings/', search_settings),
    # path('search_for_comments/', search_for_comments),
    # path('organization/', organization),
]
