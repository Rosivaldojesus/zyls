# Generated by Django 3.0 on 2021-10-19 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255), max_length=255, verbose_name='Slug'),
        ),
    ]
