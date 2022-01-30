#CRYPTO - access to data...

#https://github.com/danpaquin/coinbasepro-python


#v1

#import CRYPTO as crypto #saves the tick data
#crypto.cryptoGetTICKS() #default is for 'ETH-US'

#NOTE: #saves the Tick Data as well - to: 'crypto_tick_data.txt'
def cryptoGetTICKS(name="ETH-USD"):
  # /home/ubuntu-3/Documents/github/Crypto Game - z-py cbpro--free-tick-data.py

  # https://github.com/danpaquin/coinbasepro-python
  import time
  import cbpro  # pip install cbpro
  public_client = cbpro.PublicClient()
  '''
  {'bids': [['61052.43', '0.016054', 2]], 'asks': [['61054.64', '0.02616365', 1]], 'sequence': 30224520241, 'auction_mode': False, 'auction': None}
  '''

  """
  ETH-USD: {'trade_id': 215113549, 'price': '2602.87', 'size': '0.0208', 'time': '2022-01-29T23:59:27.764145Z', 'bid': '2602.87', 'ask': '2602.88', 'volume': '138914.88514134'}
  ETH-USD: {'trade_id': 215113555, 'price': '2602.53', 'size': '0.00380418', 'time': '2022-01-29T23:59:31.83572Z', 'bid': '2602.37', 'ask': '2602.53', 'volume': '138914.88514134'}
  ETH-USD: {'trade_id': 215113555, 'price': '2602.53', 'size': '0.00380418', 'time': '2022-01-29T23:59:31.83572Z', 'bid': '2602.37', 'ask': '2602.38', 'volume': '138914.88514134'}
  ETH-USD: {'trade_id': 215113564, 'price': '2602.22', 'size': '0.02036111', 'time': '2022-01-29T23:59:35.809571Z', 'bid': '2601.83', 'ask': '2601.84', 'volume': '138914.88514134'}
  """

  def ticker(name="ETH-USD"):
    o = public_client.get_product_ticker(product_id=name)
    string1Tick = name + ": " + str(o)
    print(string1Tick)
    saveTickData(string1Tick)
    time.sleep(2)

  # ticker('ETH-USD')

  def ticks(n, name):
    for i in range(n):
      ticker(name)

  def saveTickData(string1Tick):
    # Append-adds at last
    file1 = open("crypto_tick_data.txt", "a")  # append mode
    file1.write(f"{string1Tick} \n")
    file1.close()

  #Get 20 Ticks, default is every 2 seconds
  ticks(20, 'ETH-USD')
