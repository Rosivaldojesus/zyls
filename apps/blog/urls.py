from django.urls import path
from .views import Index, Post_Django, VisualizarPostDjango

urlpatterns = [
    path('', Index),
    path('django/', Post_Django),
    path('django/visualizar-post-django/', VisualizarPostDjango),

]