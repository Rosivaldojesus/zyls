# Generated by Django 3.0 on 2021-12-02 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0007_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='active',
            name='unitary_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
