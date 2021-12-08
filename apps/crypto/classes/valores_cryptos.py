import requests

class Cardano:

     def valor_atual_cardano(self):
          self.url = 'https://www.mercadobitcoin.net/api/ADA/ticker/'
          self.valor_cardano = requests.get(self.url).json()['ticker']["last"]
          return self.valor_cardano


class Amp:

     def valor_atual_amp(self):
          self.url = 'https://www.mercadobitcoin.net/api/AMP/ticker/'
          self.valor_amp = requests.get(self.url).json()['ticker']["last"]
          return self.valor_amp


class Bancor:

     def valor_atual_bnt(self):
          self.url = 'https://www.mercadobitcoin.net/api/BNT/ticker/'
          self.valor_bnt = requests.get(self.url).json()['ticker']["last"]
          return self.valor_bnt

class Bitcoin:

     def valor_atual_btc(self):
          self.url = 'https://www.mercadobitcoin.net/api/BTC/ticker/'
          self.valor_btc = requests.get(self.url).json()['ticker']["last"]
          return self.valor_btc


class City:

     def valor_atual_city(self):
          self.url = 'https://www.mercadobitcoin.net/api/CITYFT/ticker/'
          self.valor_city = requests.get(self.url).json()['ticker']["last"]
          return self.valor_city

class CurveDao:

     def valor_atual_crv(self):
          self.url = 'https://www.mercadobitcoin.net/api/CRV/ticker/'
          self.valor_crv = requests.get(self.url).json()['ticker']["last"]
          return self.valor_crv


class Dogecoin:

     def valor_atual_doge(self):
          self.url = 'https://www.mercadobitcoin.net/api/DOGE/ticker/'
          self.valor_doge = requests.get(self.url).json()['ticker']["last"]
          return self.valor_doge



class Mana:

     def valor_atual_mana(self):
          self.url = 'https://www.mercadobitcoin.net/api/MANA/ticker/'
          self.valor_mana = requests.get(self.url).json()['ticker']["last"]
          return self.valor_mana


class Solana:

     def valor_atual_sol(self):
          self.url = 'https://www.mercadobitcoin.net/api/SOL/ticker/'
          self.valor_sol = requests.get(self.url).json()['ticker']["last"]
          return self.valor_sol


class SushiSwap:
     def valor_atual_sushi(self):
          self.url = 'https://www.mercadobitcoin.net/api/SUSHI/ticker/'
          self.valor_sushi = requests.get(self.url).json()['ticker']["last"]
          return self.valor_sushi


class WiBX:
     def valor_atual_wbx(self):
          self.url = 'https://www.mercadobitcoin.net/api/WBX/ticker/'
          self.valor_wbx = requests.get(self.url).json()['ticker']["last"]
          return self.valor_wbx


class ZRX:
     def valor_atual_zrx(self):
          self.url = 'https://www.mercadobitcoin.net/api/ZRX/ticker/'
          self.valor_zrx = requests.get(self.url).json()['ticker']["last"]
          return self.valor_zrx