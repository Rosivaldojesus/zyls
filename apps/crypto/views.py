from django.shortcuts import render

import json
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
        context['valor_atual_cardano'] = valor_atual_cardano()
        context['percentual_ada'] = Active.objects.filter(name_crypto__crypto_symbol='ADA').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_cardano()) - 100)
        context['cardano'] = Active.objects.filter(name_crypto__crypto_symbol='ADA').annotate(
            lucro=(valor_atual_cardano() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> AMP --------------------------------------------------- """
        context['valor_atual_amp'] = valor_atual_amp()
        context['percentual_amp'] = Active.objects.filter(name_crypto__crypto_symbol='AMP').annotate(
             porcentagem=((100 / F('unitary_value')) * valor_atual_amp()) - 100)
        context['amp'] = Active.objects.filter(name_crypto__crypto_symbol='AMP').annotate(
            lucro=(valor_atual_amp() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> BNT --------------------------------------------------- """
        context['valor_atual_bnt'] = valor_atual_bnt()
        context['percentual_bnt'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_bnt()) - 100)
        context['bnt'] = Active.objects.filter(name_crypto__crypto_symbol='BNT').annotate(
            lucro=(valor_atual_bnt() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Bitcoin --------------------------------------------------- """
        context['valor_atual_btc'] = valor_atual_btc()
        context['percentual_btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_btc()) - 100)
        context['btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=(valor_atual_btc() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Manchester City FC --------------------------------------------------- """
        context['valor_atual_city'] = valor_atual_city()
        context['percentual_city'] = Active.objects.filter(name_crypto__crypto_symbol='CITYFC').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_city()) - 100)
        context['city'] = Active.objects.filter(name_crypto__crypto_symbol='CITYFC').annotate(
            lucro=(valor_atual_city() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Curve Dao Token --------------------------------------------------- """
        context['valor_atual_crv'] = valor_atual_crv()
        context['percentual_crv'] = Active.objects.filter(name_crypto__crypto_symbol='CRV').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_crv()) - 100)
        context['crv'] = Active.objects.filter(name_crypto__crypto_symbol='CRV').annotate(
            lucro=(valor_atual_crv() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Dogecoin --------------------------------------------------- """
        context['valor_atual_doge'] = valor_atual_doge()
        context['percentual_doge'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_doge()) - 100)
        context['doge'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            lucro=(valor_atual_doge() * F('quantity_crypto')) - F('purchase_value'))

        """  -->>> Kyber Network --------------------------------------------------- """
        context['valor_atual_knc'] = valor_atual_doge()
        context['percentual_knc'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_doge()) - 100)
        context['knc'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            lucro=(valor_atual_doge() * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> MANA --------------------------------------------------- """
        context['valor_atual_mana'] = valor_atual_mana()
        context['percentual_mana'] = Active.objects.filter(name_crypto__crypto_symbol='MANA').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_mana()) - 100)
        context['mana'] = Active.objects.filter(name_crypto__crypto_symbol='MANA').annotate(
            lucro=(valor_atual_mana() * F('quantity_crypto')) - F('purchase_value'))

        """"  -->>> REN --------------------------------------------------- """
        context['valor_atual_ren'] = valor_atual_sol()
        context['percentual_ren'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_sol()) - 100)
        context['ren'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            lucro=(valor_atual_sol() * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> Solana --------------------------------------------------- """
        context['valor_atual_solana'] = valor_atual_sol()
        context['percentual_sol'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_sol()) - 100)
        context['solana'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            lucro=(valor_atual_sol() * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> SUSHI --------------------------------------------------- """
        context['valor_atual_sushi'] = valor_atual_sushi()
        context['percentual_sushi'] = Active.objects.filter(name_crypto__crypto_symbol='SUSHI').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_sushi()) - 100)
        context['sushi'] = Active.objects.filter(name_crypto__crypto_symbol='SUSHI').annotate(
            lucro=(valor_atual_sushi() * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> WiBX --------------------------------------------------- """
        context['valor_atual_wbx'] = valor_atual_wbx()
        context['percentual_wbx'] = Active.objects.filter(name_crypto__crypto_symbol='WBX').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_wbx()) - 100)
        context['wbx'] = Active.objects.filter(name_crypto__crypto_symbol='WBX').annotate(
            lucro=(valor_atual_wbx() * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> ZRX --------------------------------------------------- """
        context['valor_atual_zrx'] = valor_atual_zrx()
        context['percentual_zrx'] = Active.objects.filter(name_crypto__crypto_symbol='ZRX').annotate(
            porcentagem=((100 / F('unitary_value')) * valor_atual_zrx()) - 100)
        context['zrx'] = Active.objects.filter(name_crypto__crypto_symbol='ZRX').annotate(
            lucro=(valor_atual_zrx() * F('quantity_crypto')) - F('purchase_value'))

        return context


class Dashboard(TemplateView):
    model = Active
    template_name = "crypto/dashboard.html"


    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data()

        queryset = Active.objects.all()
        names = [obj.name_crypto.name_crypto for obj in queryset]
        context['moedas'] = names

        context = {
            'names': json.dumps(names),
        }

        context
