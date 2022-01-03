from django.urls import path
from .views import Index, login_user, logout_user, submit_login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index),
    path('login/', login_user),
    path('logout/', logout_user),
    path('login/submit', submit_login),



]