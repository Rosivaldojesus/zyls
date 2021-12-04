from django.shortcuts import render
from django.db.models import F, Q
from .models import Crypto, Active
import requests

# Create your views here.
from django.views.generic import TemplateView


class Index(TemplateView):
    model = Crypto
    template_name = 'crypto/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cryptos'] = Crypto.objects.all()
        context['crypt'] = requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()
        crypt = requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()
        context['solana'] = crypt['ticker']["last"]


        return context

class Carteira(TemplateView):
    model = Active
    template_name = 'crypto/carteira.html'
    
    def get_context_data(self, **kwargs):
        context = super(Carteira, self).get_context_data()

        #Bitcoin
        bitcoin =  requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()
        bitcoin = bitcoin['ticker']["last"]
        context['bitcoin'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=( bitcoin * F('quantity_crypto')) - F('purchase_value'))


        context['crypt'] = requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()
        crypt = requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()

        solana = crypt['ticker']["last"]

        context['actives'] = Active.objects.annotate(
            lucro=( solana * F('quantity_crypto')) - F('purchase_value')
        ).order_by('name_crypto__crypto_symbol')

        context['actives'] = Active.objects.annotate(
            lucro=(F('name_crypto__value_current_cripto') * F('quantity_crypto')) - F('purchase_value')
        ).order_by('name_crypto__crypto_symbol')



        return context

class Saldos(TemplateView):
    model = Active
    template_name = "crypto/saldos.html"

    def get_context_data(self, **kwargs):
        context = super(Saldos, self).get_context_data()

        #Cardano
        cardano = requests.get('https://www.mercadobitcoin.net/api/ADA/ticker/').json()['ticker']["last"]
        context['cardano'] = Active.objects.filter(name_crypto__crypto_symbol='ADA').annotate(
            lucro=(cardano * F('quantity_crypto')) - F('purchase_value'))

        # AMP
        amp = requests.get('https://www.mercadobitcoin.net/api/AMP/ticker/').json()['ticker']["last"]
        context['amp'] = Active.objects.filter(name_crypto__crypto_symbol='AMP').annotate(
            lucro=(amp * F('quantity_crypto')) - F('purchase_value'))

        # BNT
        bnt = requests.get('https://www.mercadobitcoin.net/api/BNT/ticker/').json()['ticker']["last"]
        context['bnt'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            lucro=(bnt * F('quantity_crypto')) - F('purchase_value'))

        # BTC
        btc = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/').json()['ticker']["last"]
        context['btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=(btc * F('quantity_crypto')) - F('purchase_value'))

        # CITY
        city = requests.get('https://www.mercadobitcoin.net/api/CITY/ticker/').json()['ticker']["last"]
        context['city'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=(city * F('quantity_crypto')) - F('purchase_value'))

        return context