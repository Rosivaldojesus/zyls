import requests


def valor_atual_cardano():
    valor_cardano = requests.get('https://www.mercadobitcoin.net/api/ADA/ticker/').json()['ticker']["last"]
    return valor_cardano


def valor_atual_amp():
    valor_amp = requests.get('https://www.mercadobitcoin.net/api/AMP/ticker/').json()['ticker']["last"]
    return valor_amp


def valor_atual_bnt():
    valor_bnt = requests.get('https://www.mercadobitcoin.net/api/BNT/ticker/').json()['ticker']["last"]
    return valor_bnt


def valor_atual_btc():
    valor_btc = requests.get('https://www.mercadobitcoin.net/api/BTC/ticker/').json()['ticker']["last"]
    return valor_btc


def valor_atual_city():
    valor_city = requests.get('https://www.mercadobitcoin.net/api/CITYFT/ticker/').json()['ticker']["last"]
    return valor_city


def valor_atual_crv():
    valor_crv = requests.get('https://www.mercadobitcoin.net/api/CRV/ticker/').json()['ticker']["last"]
    return valor_crv


def valor_atual_doge():
    valor_doge = requests.get('https://www.mercadobitcoin.net/api/DOGE/ticker/').json()['ticker']["last"]
    return valor_doge

def valor_atual_knc():
    valor_knc = requests.get('https://www.mercadobitcoin.net/api/KNC/ticker/').json()['ticker']["last"]
    return valor_knc

def valor_atual_mana():
    valor_mana = requests.get('https://www.mercadobitcoin.net/api/MANA/ticker/').json()['ticker']["last"]
    return valor_mana


def valor_atual_ren():
    valor_ren = requests.get('https://www.mercadobitcoin.net/api/REN/ticker/').json()['ticker']["last"]
    return valor_ren

def valor_atual_sol():
    valor_sol = requests.get('https://www.mercadobitcoin.net/api/SOL/ticker/').json()['ticker']["last"]
    return valor_sol


def valor_atual_sushi():
    valor_sushi = requests.get('https://www.mercadobitcoin.net/api/SUSHI/ticker/').json()['ticker']["last"]
    return valor_sushi


def valor_atual_wbx():
    valor_wbx = requests.get('https://www.mercadobitcoin.net/api/WBX/ticker/').json()['ticker']["last"]
    return valor_wbx


def valor_atual_zrx():
    valor_zrx = requests.get('https://www.mercadobitcoin.net/api/ZRX/ticker/').json()['ticker']["last"]
    return valor_zrx