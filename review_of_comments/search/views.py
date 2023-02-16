from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'login.html')

# def search_for_comments(request):
#     return render(request, 'login.html')

def organization(request):
    return HttpResponse('Организация')
