#https://github.com/danpaquin/coinbasepro-python
import time
import cbpro
public_client = cbpro.PublicClient()
'''
{'bids': [['61052.43', '0.016054', 2]], 'asks': [['61054.64', '0.02616365', 1]], 'sequence': 30224520241, 'auction_mode': False, 'auction': None}
'''

def ticker(name):
    o=public_client.get_product_ticker(product_id=name)
    print(o)
    time.sleep(1)
# ticker('ETH-USD')

def ticks(n,name):
    for i in range(n):
        ticker(name)


ticks(20,'ETH-USD')


