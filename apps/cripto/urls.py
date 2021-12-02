from django.urls import path
from .views import Index

urlpatterns = [

    #ListView
    path('', Index.as_view()),


]