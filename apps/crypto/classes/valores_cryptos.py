import requests



#
# class ValorCardano():
#      url = 'https://www.mercadobitcoin.net/api/ADA/ticker/'
#      cardano = requests.get(url).json()['ticker']["last"]
#
#

class Cardano():

     # Valor atual do cardano
     def ValorAtualCardano(self):
          self.url = 'https://www.mercadobitcoin.net/api/ADA/ticker/'
          self.valor_cardano = requests.get(self.url).json()['ticker']["last"]
          return self.valor_cardano


