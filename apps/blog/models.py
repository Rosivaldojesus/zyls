from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Topicos(models.Model):
    topico = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Tópicos'
    def __str__(self):
        return "{}".format(self.topico)



class Post(models.Model):
    titulo_post = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField(default=timezone.now)
    conteudo_post = RichTextField(blank=True, null=True)
    excerto_post = RichTextField(blank=True, null=True)
    categoria_post = models.ForeignKey(Topicos, on_delete=models.DO_NOTHING)
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True)
    publicado_post = models.BooleanField(default=False)

    RESTRICAO = (
        ("Público", "Publico"),
        ("Privado", "Privado"),
    )
    restricao_post = models.CharField(max_length=7, choices=RESTRICAO, blank=False, null=False)


    class Meta:
        verbose_name_plural = 'Post'

    def get_absolute_url(self):
        return reverse('visualizar-post', kwargs={'slug': self.slug})


    def __str__(self):
        return "{}".format(self.titulo_post)


    def save(self, *args, **Kwargs):
        value = self.titulo_post
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **Kwargs)

