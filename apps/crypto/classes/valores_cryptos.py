import requests


def valor_atual_cardano():
     url = 'https://www.mercadobitcoin.net/api/ADA/ticker/'
     valor_cardano = requests.get(url).json()['ticker']["last"]
     return valor_cardano


def valor_atual_amp(self):
     url = 'https://www.mercadobitcoin.net/api/AMP/ticker/'
     valor_amp = requests.get(url).json()['ticker']["last"]
     return valor_amp



def valor_atual_bnt():
     url = 'https://www.mercadobitcoin.net/api/BNT/ticker/'
     valor_bnt = requests.get(url).json()['ticker']["last"]
     return valor_bnt






def valor_atual_btc():
     url = 'https://www.mercadobitcoin.net/api/BTC/ticker/'
     valor_btc = requests.get(url).json()['ticker']["last"]
     return valor_btc



def valor_atual_city():
     url = 'https://www.mercadobitcoin.net/api/CITYFT/ticker/'
     valor_city = requests.get(url).json()['ticker']["last"]
     return valor_city





def valor_atual_crv():
     url = 'https://www.mercadobitcoin.net/api/CRV/ticker/'
     valor_crv = requests.get(url).json()['ticker']["last"]
     return valor_crv



def valor_atual_doge():
     url = 'https://www.mercadobitcoin.net/api/DOGE/ticker/'
     valor_doge = requests.get(url).json()['ticker']["last"]
     return valor_doge





def valor_atual_mana():
     url = 'https://www.mercadobitcoin.net/api/MANA/ticker/'
     valor_mana = requests.get(url).json()['ticker']["last"]
     return valor_mana




def valor_atual_sol():
    url = 'https://www.mercadobitcoin.net/api/SOL/ticker/'
    valor_sol = requests.get(url).json()['ticker']["last"]
    return valor_sol



def valor_atual_sushi():
     url = 'https://www.mercadobitcoin.net/api/SUSHI/ticker/'
     valor_sushi = requests.get(url).json()['ticker']["last"]
     return valor_sushi



def valor_atual_wbx():
    url = 'https://www.mercadobitcoin.net/api/WBX/ticker/'
    valor_wbx = requests.get(url).json()['ticker']["last"]
    return valor_wbx



def valor_atual_zrx():
    url = 'https://www.mercadobitcoin.net/api/ZRX/ticker/'
    valor_zrx = requests.get(url).json()['ticker']["last"]
    return valor_zrx