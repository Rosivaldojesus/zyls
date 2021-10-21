from django.urls import path
from .views import PostDjangoCreateView, PostDjangoDetailView, PostListView, PostDetailView, PostUpdateView
from .views import PostDjango, VisualizarPostDjango

urlpatterns = [
    path('django/', PostDjango),
    path('django/visualizar-post-django/', VisualizarPostDjango),


    # CreateView
    path('django/criar-post/', PostDjangoCreateView.as_view(), name='criar-post'),


    # UpdateView
    path('blog/<slug:slug>/', PostUpdateView.as_view(), name='editar-post'),

    # ListView
    path('', PostListView.as_view(), name='index'),

    # DetailView
    path('<slug:slug>/', PostDetailView.as_view(), name='visualizar-post'),


]