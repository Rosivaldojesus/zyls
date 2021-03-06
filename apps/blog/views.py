from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import Comentarios, Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.db.models import Q, Count, Case, When
from time import time


# Create your views here.
class PostListView(ListView):

    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    tempo_inicial = time()
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentarios__publicado_comentario=True, then=1)
                )
            )
        )
        return qs

    tempo_final = time()

    print(f'Tempo de execução: {tempo_final - tempo_inicial}' )


class PostDetalhesView(DetailView):
    model = Post
    template_name= 'blog/post-detalhes.html'


class PostCategoriasView(PostListView):
    template_name = 'blog/post-categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs
        qs = qs.filter(categoria_post__nome_categoria__iexact=categoria)
        return qs


class PostBuscaView(PostListView):
    template_name = 'blog/post-busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        if not termo:
            return qs
        qs = qs.filter(Q(titulo_post__icontains=termo))
        return qs


class PostDjangoCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = "blog/criar-post.html"
    form_class = PostCreateForm
    success_url = '/blog/'
    success_message = "%(titulo_post)s, foi criado com sucesso!!!"

    def form_valid(self, form):
        if form.is_valid():
            #form.instance.autor_post = self.object
            form.instance.autor_post = self.request.user
            form.save()
            return super(PostDjangoCreateView, self).form_valid(form)
        else:
            return super(PostDjangoCreateView, self).form_invalid(form)



class PostDetailView(DetailView):
    # specify the model to use
    model = Post
    template_name = 'blog/visualizar-post.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView,
                        self).get_context_data(*args, **kwargs)
        return context


class PostUpdateView(UpdateView):
    model = Post # A tabela do banco de dados
    form_class = PostUpdateForm # Form for Update
    template_name = 'blog/editar-post.html'  # templete for updating
    template_name_suffix = 'editar-post'
    success_url = "blog/"  # return após atualizar


class PostDeleteView(DeleteView):
    template_name = 'employee/employee_delete.html'
    queryset = Post.objects.all()

    def get_success_url(self):
        return reverse('/blog/')

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def delete_modal_view(request):
        return render(request, "deletar-post.html")


def DeletarPost(request, id=None):
    servico = get_object_or_404(Post, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect('/blog/')
    return redirect('/blog/')





def AddPost(request):
    form = PostCreateForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.criado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço adicionado com sucesso!')
        return redirect('/servicos/')
    else:
        form = PostCreateForm()
    return render(request, 'services/cadastro-servico.html', {'form': form})

def PostDjango(request):
    posts = Post.objects.all()
    return render(request, 'blog/__django.html',
                  {'posts':posts,
                   })

def VisualizarPostDjango(request):
    post = request.GET.get('id')
    if post:
        post = Post.objects.get(id=post)
    return render(request, 'blog/visualizar-post-django(excluir).html',{'post': post})