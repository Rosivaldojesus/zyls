from django.urls import path

from .views import PostDjangoCreateView
from .views import Index, PostDjango, VisualizarPostDjango

urlpatterns = [
    path('', Index),
    path('django/', PostDjango),
    path('django/visualizar-post-django/', VisualizarPostDjango),

    path('django/criar-post/', PostDjangoCreateView.as_view(), name='criar-post'),





]