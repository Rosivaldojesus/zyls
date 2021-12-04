from django.urls import path
from .views import Index, Carteira, Saldos

urlpatterns = [

    #ListView
    path('', Index.as_view()),
    path('carteira/', Carteira.as_view()),
    path('saldos/', Saldos.as_view()),


]