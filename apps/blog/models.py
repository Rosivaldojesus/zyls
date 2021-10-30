from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome da categoria')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{}'.format(self.nome_categoria)





class Post(models.Model):
    titulo_post = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo_post = RichTextField(blank=True, null=True)
    excerto_post = RichTextField(blank=True, null=True)
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True)
    publicado_post = models.BooleanField(default=False)

    RESTRICAO = (
        ("Público", "Publico"),
        ("Privado", "Privado"),
    )
    restricao_post = models.CharField(max_length=7, choices=RESTRICAO, blank=False, null=False)


    class Meta:
        verbose_name_plural = 'Post'

    #Criar automaticamente o slug
    def save(self, *args, **Kwargs):
        value = self.titulo_post
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **Kwargs)

    #Chamada a visualização baseada no slug
    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('visualizar-post', kwargs=kwargs)
        #return reverse('visualizar-post', kwargs={'slug': self.slug})


    def __str__(self):
        return "{}".format(self.titulo_post)




class Comentarios(models.Model):
    nome_comentario = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome Comentário')
    email_comentario = models.EmailField(verbose_name='E-mail do Comentários')
    comentario = RichTextField(blank=True, null=True, verbose_name='Comentário')
    post_comentario = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Nome do usuário')
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
    
    def __str__(self):
        return "{}".format(self.nome_comentario)





class Topicos(models.Model):
    topico = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Tópicos'
    def __str__(self):
        return "{}".format(self.topico)
