from django.contrib import admin
from .models import Crypto, CategoryCripto

# Register your models here.

admin.site.register(CategoryCripto)
admin.site.register(Crypto)