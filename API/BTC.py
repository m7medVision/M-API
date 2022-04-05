import requests
import json


def get_btc_price():
    url = 'https://production.api.coindesk.com/v2/tb/price/ticker?assets=BTC'
    response = requests.get(url)
    btc_price = json.loads(response.text)
    return btc_price['data']['BTC']['ohlc']['c']
