from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm

# Create your views here.
class PostDjangoCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = "blog/criar-post.html"
    form_class = PostCreateForm
    success_url = '/blog/'
    success_message = "%(titulo_post)s, foi criado com sucesso!!!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            titulo_post=self.object.titulo_post,
        )

    def form_valid(self, form):
        form.instance.autor_post = self.request.user
        return super().form_valid(form)


class PostDjangoDetailView(DetailView):
    model = Post



class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter()
    context_object_name = 'posts'


class PostDetailView(DetailView):
    # specify the model to use
    model = Post
    template_name = 'blog/visualizar-post.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView,
                        self).get_context_data(*args, **kwargs)
        # add extra field
        context["category"] = "MISC"
        return context






def PostDjango(request):
    posts = Post.objects.all()
    return render(request, 'blog/django.html',
                  {'posts':posts,
                   })

def VisualizarPostDjango(request):
    post = request.GET.get('id')
    if post:
        post = Post.objects.get(id=post)
    return render(request, 'blog/visualizar-post-django.html',{'post': post})