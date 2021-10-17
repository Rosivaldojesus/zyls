from django.shortcuts import render
from .models import Post

# Create your views here.
def Index(request):
    return render(request, 'blog/index.html')

def Post_Django(request):
    posts = Post.objects.all()
    return render(request, 'blog/django.html',
                  {'posts':posts,
                   })

def VisualizarPostDjango(request):
    post = request.GET.get('id')
    if post:
        post = Post.objects.get(id=post)
    return render(request, 'blog/visualizar-post-django.html',{'post': post})