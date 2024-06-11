from . import views
from django.urls import path

app_name = 'authz'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]