from . import views
from django.urls import path

app_name = 'authz'


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.signout, name='signout'),
    path('user_home/', views.user_home, name='user_home'),
]