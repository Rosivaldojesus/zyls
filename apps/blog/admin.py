from django.contrib import admin
from ..blog.models import Topicos

from .models import Categoria,Post,  Comentarios

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria')
    
admin.site.register(Categoria, CategoriaAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_post','categoria_post' ,'restricao_post','publicado_post')
    search_fields = ('titulo_post', )
    list_editable = ('restricao_post', 'publicado_post' )
    list_display_links = ('id', 'titulo_post')
admin.site.register(Post, PostAdmin)


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comentario', 'email_comentario', 'publicado_comentario' )
    list_editable = ('publicado_comentario', )
    list_display_links = ('id', 'nome_comentario', 'email_comentario')
admin.site.register(Comentarios, ComentariosAdmin)

#---------------------------------------------------
#---------------------------------------------------
#---------------------------------------------------
admin.site.register(Topicos)
