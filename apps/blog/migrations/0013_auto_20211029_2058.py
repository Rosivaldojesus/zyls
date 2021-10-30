# Generated by Django 3.0 on 2021-10-29 23:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20211029_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='comentario',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Comentário'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='email_comentario',
            field=models.EmailField(max_length=254, verbose_name='E-mail do Comentários'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='post_comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='publicado_comentario',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='usuario_comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Nome do usuário'),
        ),
    ]
