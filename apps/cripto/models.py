from django.db import models

# Create your models here.
class CategoryCripto(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='Nome da Categoria')

    class Meta:
        verbose_name_plural = 'Categoria da Cripto'

    def __str__(self):
        return self.name_category


class Crypto(models.Model):
    name_crypto = models.CharField(max_length=100, verbose_name='Nome da Cripto')
    value_current_cripto = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    crypto_symbol = models.CharField(max_length=10, verbose_name='Simbolo da Crypto')
    category = models.ForeignKey(CategoryCripto, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Criptomoeda'

    def __str__(self):
        return self.name_crypto