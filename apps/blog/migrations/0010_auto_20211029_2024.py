# Generated by Django 3.0 on 2021-10-29 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Categoria'),
        ),
    ]
