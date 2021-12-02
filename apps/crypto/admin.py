from django.contrib import admin
from .models import Crypto, CategoryCripto

# Register your models here.



admin.site.register(CategoryCripto)

class CryptoAdmin(admin.ModelAdmin):
    list_display = ('name_crypto', 'value_current_cripto', 'crypto_symbol', 'category')
admin.site.register(Crypto, CryptoAdmin)