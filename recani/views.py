import json
from .recommendation import UCB
from authz.models import GeneralData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .session_helpers import initialize_user_history, update_user_history


@require_GET
def search_anime(request):
    name = request.GET.get('name')
    payload = []
    
    if name:
        names_english_objs = GeneralData.objects.filter(name_english__icontains=name)
        for obj in names_english_objs:
            payload.append(obj.name_english)

    return JsonResponse({'status': 200, 'data': payload})


@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'recani/initializations.html')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        show1 = data.get('show1')
        show2 = data.get('show2')
        show3 = data.get('show3')
        show1_rating = int(data.get('show1_rating'))
        show2_rating = int(data.get('show2_rating'))
        show3_rating = int(data.get('show3_rating'))

        # Ensure that these shows exist
        show1_obj = GeneralData.objects.filter(name_english=show1).first()
        show2_obj = GeneralData.objects.filter(name_english=show2).first()
        show3_obj = GeneralData.objects.filter(name_english=show3).first()
        
        show1 = show1_obj.unique_id
        show2 = show2_obj.unique_id
        show3 = show3_obj.unique_id

        print('HOME : ',  show1, show2, show3, show1_rating, show2_rating, show3_rating)

        # Use helper function to initialize session data
        initialize_user_history(request.session, show1, show2, show3, show1_rating, show2_rating, show3_rating)

        return JsonResponse({'status': 'success', 'message': 'Data processed successfully'})



@login_required
def get_recommendations(request):

    if request.method == 'GET':
        print('GET/get_recommendations ================')
        recommendations = UCB(request.session)
        context = {
            'data' : []
        }

        for anime in recommendations:
            context['data'].append(GeneralData.objects.filter(unique_id=anime).first())

        return render(request, 'recani/get_recommendations.html', context=context)
    else :
        print('POST/get_recommendations ================')
        show1_rating = int(request.POST.get('show1_rating'))
        show2_rating = int(request.POST.get('show2_rating'))
        show3_rating = int(request.POST.get('show3_rating'))

        print(show1_rating, show2_rating, show3_rating)

        update_user_history(request.session, show1_rating, show2_rating, show3_rating)
        
        recommendations = UCB(request.session)
        context = {
            'data' : []
        }

        for anime in recommendations:
            context['data'].append(GeneralData.objects.filter(unique_id=anime).first())

        return render(request, 'recani/get_recommendations.html', context=context)




def show_detail(request, id):
    show = get_object_or_404(GeneralData, unique_id=id)
    return render(request, 'recani/show_details.html', {'show':show})