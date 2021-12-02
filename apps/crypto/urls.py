from django.urls import path
from .views import Index, Carteira

urlpatterns = [

    #ListView
    path('', Index.as_view()),
    path('carteira/', Carteira.as_view()),


]