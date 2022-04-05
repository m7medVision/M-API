# get ETH priece
import requests
import json


def get_eth_price():
    url = 'https://production.api.coindesk.com/v2/tb/price/ticker?assets=ETH'
    response = requests.get(url)
    eth_price = json.loads(response.text)
    return eth_price['data']['ETH']['ohlc']['c']


# print(get_btc_price())
print(get_eth_price())
