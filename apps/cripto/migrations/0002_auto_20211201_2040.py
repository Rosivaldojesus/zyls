# Generated by Django 3.0 on 2021-12-01 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criptos',
            name='valor_atual_cripto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
