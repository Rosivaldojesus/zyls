# Generated by Django 3.0 on 2021-12-27 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0014_auto_20211202_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active',
            name='purchase_value',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='active',
            name='unitary_value',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]
