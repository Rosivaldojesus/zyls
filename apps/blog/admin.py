from django.contrib import admin
from ..blog.models import Topicos, Post

# Register your models here.
admin.site.register(Topicos)
admin.site.register(Post)