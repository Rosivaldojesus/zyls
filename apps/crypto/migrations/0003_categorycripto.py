# Generated by Django 3.0 on 2021-12-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0002_auto_20211201_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCripto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100, verbose_name='Nome da Categoria')),
            ],
            options={
                'verbose_name_plural': 'Categoria da Cripto',
            },
        ),
    ]
