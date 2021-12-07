import requests

class Cardano:
     """ Valores referentes a Cardano"""
     def valor_atual_cardano(self):
          self.url = 'https://www.mercadobitcoin.net/api/ADA/ticker/'
          self.valor_cardano = requests.get(self.url).json()['ticker']["last"]
          return self.valor_cardano


class Amp:
     """ AMP """
     def valor_atual_amp(self):
          self.url = 'https://www.mercadobitcoin.net/api/AMP/ticker/'
          self.valor_amp = requests.get(self.url).json()['ticker']["last"]
          return self.valor_amp