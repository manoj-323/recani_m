from django.shortcuts import render, redirect
from .models import GeneralData, AdminChoices, Saved_anime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as loginUser, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def home(request):
    if request.method == 'GET':
        admins_recommendations = AdminChoices.objects.all()
        anime_data = []
        for i in admins_recommendations:
            anime_data.append(GeneralData.objects.get(unique_id=i.index))
        context = {
            'anime_data' : anime_data,
        }
        return render(request, 'authz/home.html', context=context)
    else:
        return render(request, 'authz/home.html')

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        data = {
            'form' : form,
        }
        return render(request, 'authz/login.html', context=data)
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request=request, user=user)
                return redirect('authz:user_home')
        else:
            data = {
            'form' : form,
            }
            return render(request, 'authz/login.html', context=data)

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        data = {
            "form" : form,
        }
        return render(request, 'authz/signup.html', context=data)
    
    else:
        form = UserCreationForm(request.POST)
        data = {
            "form" : form,
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('authz:login')
        else:
            return render(request, 'authz/signup.html', context=data)

def signout(request):
    request.session.flush()
    logout(request=request)
    return redirect('authz:home')

@login_required
def user_home(request):
    saved_anime = Saved_anime.objects.filter(user=request.user)
    recent_activities = request.session.get('user_history_dict', {}).get('already_recommended', [])

    anime_data = []
    for i in recent_activities:
        anime_data.append(GeneralData.objects.get(unique_id=i))
    
    context = {
        'saved_anime': saved_anime,
        'recent_activities': anime_data
    }
    return render(request, 'authz/user_home.html', context=context)