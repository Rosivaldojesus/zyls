# Generated by Django 3.0 on 2021-10-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20211019_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255)),
        ),
    ]
