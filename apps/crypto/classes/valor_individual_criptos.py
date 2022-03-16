import requests


def valor_atual_cardano():
    valor_cardano = requests.get('https://www.mercadobitcoin.net/api/ADA/ticker/').json()['ticker']["last"]
    return valor_cardano