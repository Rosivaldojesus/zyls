from django.shortcuts import render
from django.db.models import F, Q
from .models import Crypto, Active
import requests

from .classes.valores_cryptos import Cardano


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
        valor_cardano = Cardano.valor_atual_cardano(self)

        #Cardano
        context['valor_atual_cardano'] = Cardano.valor_atual_cardano(self)
        context['percentual'] = Active.objects.filter(name_crypto__crypto_symbol='ADA')\
            .annotate(lucro=(valor_cardano * 10) - F('purchase_value'))

        context['cardano'] = Active.objects.filter(name_crypto__crypto_symbol='ADA')\
        .annotate(lucro=(valor_cardano * F('quantity_crypto')) - F('purchase_value'))



        # AMP
        amp = requests.get('https://www.mercadobitcoin.net/api/AMP/ticker/').json()['ticker']["last"]
        context['valor_atual_amp'] = amp
        context['amp'] = Active.objects.filter(name_crypto__crypto_symbol='AMP').annotate(
            lucro=(amp * F('quantity_crypto')) - F('purchase_value'))

        # BNT
        bnt = requests.get('https://www.mercadobitcoin.net/api/BNT/ticker/').json()['ticker']["last"]
        context['valor_atual_bnt'] = bnt
        context['bnt'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            lucro=(bnt * F('quantity_crypto')) - F('purchase_value'))

        # BTC
        btc = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/').json()['ticker']["last"]
        context['valor_atual_btc'] = btc
        context['btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=(btc * F('quantity_crypto')) - F('purchase_value'))

        # CITY
        city = requests.get('https://www.mercadobitcoin.net/api/CITYFT/ticker/').json()['ticker']["last"]
        context['valor_atual_city'] = city
        context['city'] = Active.objects.filter(name_crypto__crypto_symbol='CITY').annotate(
            lucro=(city * F('quantity_crypto')) - F('purchase_value'))

        # CRV
        crv = requests.get('https://www.mercadobitcoin.net/api/CRV/ticker/').json()['ticker']["last"]
        context['valor_atual_crv'] = crv
        context['crv'] = Active.objects.filter(name_crypto__crypto_symbol='CRV').annotate(
            lucro=(crv * F('quantity_crypto')) - F('purchase_value'))

        # DOGE
        doge = requests.get('https://www.mercadobitcoin.net/api/DOGE/ticker/').json()['ticker']["last"]
        context['valor_atual_doge'] = doge
        context['doge'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            lucro=(doge * F('quantity_crypto')) - F('purchase_value'))

        # MANA
        mana = requests.get('https://www.mercadobitcoin.net/api/MANA/ticker/').json()['ticker']["last"]
        context['valor_atual_mana'] = mana
        context['mana'] = Active.objects.filter(name_crypto__crypto_symbol='MANA').annotate(
            lucro=(mana * F('quantity_crypto')) - F('purchase_value'))

        # SOLANA
        solana = requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()['ticker']["last"]
        context['valor_atual_solana'] = solana
        context['solana'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            lucro=(solana * F('quantity_crypto')) - F('purchase_value'))

        # SUSHI
        sushi = requests.get('https://www.mercadobitcoin.net/api/SUSHI/ticker/').json()['ticker']["last"]
        context['valor_atual_sushi'] = sushi
        context['sushi'] = Active.objects.filter(name_crypto__crypto_symbol='SUSHI').annotate(
            lucro=(sushi * F('quantity_crypto')) - F('purchase_value'))

        # WBX
        wbx = requests.get('https://www.mercadobitcoin.net/api/WBX/ticker/').json()['ticker']["last"]
        context['valor_atual_wb'] = wbx
        context['wbx'] = Active.objects.filter(name_crypto__crypto_symbol='WBX').annotate(
            lucro=(wbx * F('quantity_crypto')) - F('purchase_value'))

        # ZRX
        zrx = requests.get('https://www.mercadobitcoin.net/api/ZRX/ticker/').json()['ticker']["last"]
        context['valor_atual_zrx'] = zrx
        context['zrx'] = Active.objects.filter(name_crypto__crypto_symbol='ZRX').annotate(
            lucro=(zrx * F('quantity_crypto')) - F('purchase_value'))


        return context