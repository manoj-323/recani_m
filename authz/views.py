from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'authz/home.html')

def signup(request):
    return render(request, 'authz/signup.html')

def login(request):
    return render(request, 'authz/login.html')

# def logout(request):
#     return render(request, 'authz/home.html')