from django.shortcuts import render
from .models import GeneralData, AdminChoices

# Create your views here.

def temp(request):
    if request.method == 'GET':
        anime_data =  GeneralData.objects.select_related('studio', 'demographic', 'rating', 'source', 'typeof').get(unique_id=1)
        genres = [x.name for x in anime_data.genre.all()]
        context = {
            'anime_data' : anime_data,
            'genres' : genres
        }
        return render(request, 'authz/temp.html', context=context)
    else:
        return render(request, 'authz/temp.html')

def home(request):
    if request.method == 'GET':
        admins_recommendations = AdminChoices.objects.all()
        anime_data = []
        for i in admins_recommendations:
            anime_data.append(GeneralData.objects.get(unique_id=i.index))
        print(anime_data)
        context = {
            'anime_data' : anime_data,
        }
        return render(request, 'authz/home.html', context=context)
    else:
        return render(request, 'authz/home.html')

def signup(request):
    return render(request, 'authz/signup.html')

def login(request):
    return render(request, 'authz/login.html')

# def logout(request):
#     return render(request, 'authz/home.html')