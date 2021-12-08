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
        context['percentual_btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            porcentagem=((100 / F('unitary_value')) * Bitcoin.valor_atual_btc(self)) - 100)
        context['btc'] = Active.objects.filter(name_crypto__crypto_symbol='BTC').annotate(
            lucro=(Bitcoin.valor_atual_btc(self) * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Manchester City FC --------------------------------------------------- """
        context['valor_atual_city'] = City.valor_atual_city(self)
        context['percentual_city'] = Active.objects.filter(name_crypto__crypto_symbol='CITYFC').annotate(
            porcentagem=((100 / F('unitary_value')) * City.valor_atual_city(self)) - 100)
        context['city'] = Active.objects.filter(name_crypto__crypto_symbol='CITYFC').annotate(
            lucro=(City.valor_atual_city(self) * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Curve Dao Token --------------------------------------------------- """
        context['valor_atual_crv'] = CurveDao.valor_atual_crv(self)
        context['percentual_crv'] = Active.objects.filter(name_crypto__crypto_symbol='CRV').annotate(
            porcentagem=((100 / F('unitary_value')) * CurveDao.valor_atual_crv(self)) - 100)
        context['crv'] = Active.objects.filter(name_crypto__crypto_symbol='CRV').annotate(
            lucro=(CurveDao.valor_atual_crv(self) * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> Dogecoin --------------------------------------------------- """
        context['valor_atual_doge'] = Dogecoin.valor_atual_doge(self)
        context['percentual_doge'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            porcentagem=((100 / F('unitary_value')) * Dogecoin.valor_atual_doge(self)) - 100)
        context['doge'] = Active.objects.filter(name_crypto__crypto_symbol='DOGE').annotate(
            lucro=(Dogecoin.valor_atual_doge(self) * F('quantity_crypto')) - F('purchase_value'))


        """  -->>> MANA --------------------------------------------------- """
        context['valor_atual_mana'] = Mana.valor_atual_mana(self)
        context['percentual_mana'] = Active.objects.filter(name_crypto__crypto_symbol='MANA').annotate(
            porcentagem=((100 / F('unitary_value')) * Mana.valor_atual_mana(self)) - 100)
        context['mana'] = Active.objects.filter(name_crypto__crypto_symbol='MANA').annotate(
            lucro=(Mana.valor_atual_mana(self) * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> Solana --------------------------------------------------- """
        context['valor_atual_solana'] = Solana.valor_atual_sol(self)
        context['percentual_sol'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            porcentagem=((100 / F('unitary_value')) * Solana.valor_atual_sol(self)) - 100)
        context['solana'] = Active.objects.filter(name_crypto__crypto_symbol='SOL').annotate(
            lucro=(Solana.valor_atual_sol(self) * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> SUSHI --------------------------------------------------- """
        context['valor_atual_sushi'] = SushiSwap.valor_atual_sushi(self)
        context['percentual_suhi'] = Active.objects.filter(name_crypto__crypto_symbol='SUSHI').annotate(
            porcentagem=((100 / F('unitary_value')) * SushiSwap.valor_atual_sushi(self)) - 100)
        context['sushi'] = Active.objects.filter(name_crypto__crypto_symbol='SUSHI').annotate(
            lucro=(SushiSwap.valor_atual_sushi(self) * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> WiBX --------------------------------------------------- """
        context['valor_atual_wbx'] = WiBX.valor_atual_wbx(self)
        context['percentual_wbx'] = Active.objects.filter(name_crypto__crypto_symbol='WBX').annotate(
            porcentagem=((100 / F('unitary_value')) * WiBX.valor_atual_wbx(self)) - 100)
        context['wbx'] = Active.objects.filter(name_crypto__crypto_symbol='WBX').annotate(
            lucro=(WiBX.valor_atual_wbx(self) * F('quantity_crypto')) - F('purchase_value'))


        """"  -->>> ZRX --------------------------------------------------- """
        context['valor_atual_zrx'] = ZRX.valor_atual_zrx(self)
        context['percentual_wbx'] = Active.objects.filter(name_crypto__crypto_symbol='ZRX').annotate(
            porcentagem=((100 / F('unitary_value')) * ZRX.valor_atual_zrx(self)) - 100)
        context['zrx'] = Active.objects.filter(name_crypto__crypto_symbol='ZRX').annotate(
            lucro=(ZRX.valor_atual_zrx(self) * F('quantity_crypto')) - F('purchase_value'))


        return context