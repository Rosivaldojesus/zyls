from django.shortcuts import render
from django.db.models import F, Q
from .models import Crypto, Active
import requests

from .classes.valores_cryptos import *


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

        """  -->> Cardano ---------------------------------------------------------"""
        context['valor_atual_cardano'] = Cardano.valor_atual_cardano(self)
        context['percentual_ada'] = Active.objects.filter(name_crypto__crypto_symbol='ADA').annotate(
            porcentagem=((100 / F('unitary_value')) * Cardano.valor_atual_cardano(self)) - 100)
        context['cardano'] = Active.objects.filter(name_crypto__crypto_symbol='ADA').annotate(
            lucro=(Cardano.valor_atual_cardano(self) * F('quantity_crypto')) - F('purchase_value'))

        """  -->>> AMP --------------------------------------------------- """
        context['valor_atual_amp'] = Amp.valor_atual_amp(self)
        context['percentual_amp'] = Active.objects.filter(name_crypto__crypto_symbol='AMP').annotate(
             porcentagem=((100 / F('unitary_value')) * Amp.valor_atual_amp(self)) - 100)
        context['amp'] = Active.objects.filter(name_crypto__crypto_symbol='AMP').annotate(
            lucro=(Amp.valor_atual_amp(self) * F('quantity_crypto')) - F('purchase_value'))



        """  -->>> BNT --------------------------------------------------- """
        context['valor_atual_bnt'] = Bancor.valor_atual_bnt(self)
        context['percentual_bnt'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            porcentagem=((100 / F('unitary_value')) * Bancor.valor_atual_bnt(self)) - 100)

        context['bnt'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            lucro=(Bancor.valor_atual_bnt(self) * F('quantity_crypto')) - F('purchase_value'))

        """  -->>> Bitcoin --------------------------------------------------- """
        context['valor_atual_btc'] = Bitcoin.valor_atual_btc(self)
        context['percentual_btc'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            porcentagem=((100 / F('unitary_value')) * Bitcoin.valor_atual_btc(self)) - 100)
        context['btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=(Bitcoin.valor_atual_btc(self) * F('quantity_crypto')) - F('purchase_value'))

        """  -->>> Manchester City FC --------------------------------------------------- """
        context['valor_atual_city'] = City.valor_atual_city(self)
        context['percentual_city'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            porcentagem=((100 / F('unitary_value')) * City.valor_atual_city(self)) - 100)
        context['city'] = Active.objects.filter(name_crypto__crypto_symbol='CITY').annotate(
            lucro=(City.valor_atual_city(self) * F('quantity_crypto')) - F('purchase_value'))

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