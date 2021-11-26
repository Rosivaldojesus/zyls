from django.urls import path
from .views import PostListView, VisualizarPostDjango, DeletarPost, AddPost, PostDeleteView, PostDjangoCreateView, \
 PostUpdateView, PostCategoriasView, PostBuscaView, PostDetalhesView, PostDjango

urlpatterns = [

    #ListView
    path('', PostListView.as_view(), name='index'),

     
    # UpdateView
    path('blog/<slug:slug>/', PostUpdateView.as_view(), name='editar-post'),










    path('django/visualizar-post-django/', VisualizarPostDjango),

    path('django/deletar-post/<int:id>', DeletarPost),


    path('blog/add-posts/', AddPost),

    # DeleteView
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='deletar-post'),

    # CreateView
    path('criar-post/', PostDjangoCreateView.as_view(), name='criar-post'),




    # ListView

    path('post-categoria/<str:categoria>', PostCategoriasView.as_view(), name='post-categoria'),
    path('busca/', PostBuscaView.as_view(), name='post-busca'),

    # DetailView
    path('post/<int:pk>', PostDetalhesView.as_view(), name='post-detalhes'),



    path('django/', PostDjango),

]