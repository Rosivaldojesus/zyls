from django.urls import path
from .views import Graph, Graph_a, Graph_b

urlpatterns = [

    #ListView
    path('', Graph.as_view()),
    path('graph_a/', Graph_a.as_view(), name='graph_a'),
    path('graph_b/', Graph_b),


]