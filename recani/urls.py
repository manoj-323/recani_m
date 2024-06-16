from django.urls import path
from . import views

app_name = 'recani'
urlpatterns = [
    path('initialization-page/', views.home, name='initialization-page'),
    path('search/', views.search_anime, name='search_anime'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
    path('show_detail/<int:id>/', views.show_detail, name='show_detail'),
    path('save_anime/', views.save_anime, name='save_anime'),
  ]