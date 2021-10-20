from django.urls import path
from .views import PostDjangoCreateView, PostDjangoDetailView, PostListView, PostDetailView
from .views import PostDjango, VisualizarPostDjango

urlpatterns = [
    path('django/', PostDjango),
    path('django/visualizar-post-django/', VisualizarPostDjango),

    path('django/criar-post/', PostDjangoCreateView.as_view(), name='criar-post'),
    path('', PostListView.as_view(), name='index'),
    path('<slug:slug>/', PostDetailView.as_view(), name='visualizar-post'),

    path('<slug:slug>/', PostDjangoDetailView.as_view(), name='article-detail'),
]