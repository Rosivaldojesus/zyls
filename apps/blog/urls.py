from django.urls import path
from .views import PostDjangoCreateView, PostDjangoDetailView, PostListView, PostDetailView, PostUpdateView
from .views import PostDjango, VisualizarPostDjango, DeletarPost, AddPost, PostDeleteView

from.views import PostCategoriasView

urlpatterns = [
    path('django/', PostDjango),
    path('django/visualizar-post-django/', VisualizarPostDjango),

    path('django/deletar-post/<int:id>', DeletarPost),


    path('blog/add-posts/', AddPost),

    # DeleteView
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='deletar-post'),

    # CreateView
    path('criar-post/', PostDjangoCreateView.as_view(), name='criar-post'),


    # UpdateView
    path('blog/<slug:slug>/', PostUpdateView.as_view(), name='editar-post'),

    # ListView
    path('', PostListView.as_view(), name='index'),
    path('post-categoria/<str:categoria>', PostCategoriasView.as_view(), name='post-categoria'),

    # DetailView
    path('<slug:slug>/', PostDetailView.as_view(), name='visualizar-post'),


]