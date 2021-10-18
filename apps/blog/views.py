from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from .models import Post
from .forms import PostCreateForm

# Create your views here.
def Index(request):
    return render(request, 'blog/index.html')


class PostDjangoCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = "blog/criar-post.html"
    form_class = PostCreateForm
    success_url = '/blog/'
    success_message = "%(titulo_post)s foi criado com sucesso!!!"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.titulo_post,
        )

    def form_valid(self, form):
        form.instance.autor_post = self.request.user
        return super().form_valid(form)



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