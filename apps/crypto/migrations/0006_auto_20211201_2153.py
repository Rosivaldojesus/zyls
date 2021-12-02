# Generated by Django 3.0 on 2021-12-02 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_criptos_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_crypto', models.CharField(max_length=100, verbose_name='Nome da Cripto')),
                ('value_current_cripto', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('crypto_symbol', models.CharField(max_length=10, verbose_name='Simbolo da Crypto')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='crypto.CategoryCripto')),
            ],
            options={
                'verbose_name_plural': 'Criptomoeda',
            },
        ),
        migrations.DeleteModel(
            name='Criptos',
        ),
    ]