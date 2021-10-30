from django import forms
from .models import Post





class PostCreateForm(forms.ModelForm):
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