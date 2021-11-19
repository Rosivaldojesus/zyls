from django import forms
from .models import Post
from django.forms import ModelForm
from django.core.exceptions import ValidationError



class PostCreateForm(ModelForm):  

    class Meta:
        model = Post
        fields = ['titulo_post',
                  'excerto_post',
                  'conteudo_post',
                  'categoria_post',
                  'imagem_post',
                  'publicado_post',
                  'restricao_post'
                  ]

    


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo_post',
                  'excerto_post',
                  'conteudo_post',
                  'categoria_post',
                  'imagem_post',
                  'publicado_post',
                  'restricao_post'
                  ]