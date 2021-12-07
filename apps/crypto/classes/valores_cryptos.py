import requests
from django.db.models import F, Q
from ..models import Active


class Cardano:

     def valor_atual_cardano(self):
          url = 'https://www.mercadobitcoin.net/api/ADA/ticker/'
          self.valor_cardano = requests.get(url).json()['ticker']["last"]
          return self.valor_cardano

     def percentual_cardano(self, **kwargs):
          context = super(Cardano, self).percentual_cardano()


          return context



