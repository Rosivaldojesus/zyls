from django.shortcuts import render
from .models import Crypto

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    model = Crypto
    template_name = 'cripto/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cryptos'] = Crypto.objects.all()
        return context

