#CRYPTO - access to data... plotting

# show 4 on one board
# import PlotGRAPHS as p
# p.showNiceCryptoView("ETH-USD")

# c.cryptoStartup()
#
# high, low = c.getNdaysHighLow(crypto="ETH-USD",days=7)

# c.cryptoGetTICKS() #default is for 'ETH-US'

# c.getCryptoCSVmultiple()
# c.downloadCryptoCSV3(crypto="ETH-USD")
# c.downloadCryptoCSV2(crypto="ETH-USD")
# c.downloadStockCSV1(stock="AAPL")

# num = c.round_down(n=1.2345, decimals=2)
# num = c.dollars(n=1111.2345)


#----------------------------------------------





#----------------------------------
# import CRYPTO as c
# c.cryptoStartup()
def cryptoStartup():
  import CRYPTO as c
  c.getCryptoInfo(cryptoName="ETH", currency="USD")  # crypto.getCryptoInfo()
  c.getCryptoInfo(cryptoName="BTC", currency="USD")  # crypto.getCryptoInfo()

  # import CRYPTO as c
  crypto1 = "ETH-USD"
  print("-----------------")
  high1, low1 = c.getNdaysHighLow(crypto=crypto1, days=7)
  print(f"High for {crypto1} - 7 days: ${high1}\n")
  print(f"Low for {crypto1} - 7 days: ${low1}")
  percentage1 = c.round_down(100 * (float(high1.replace(",", "")) / float(low1.replace(",", ""))) - 100)
  print(f"Percentage change: {percentage1} %")

  print("-----------------")
  high2, low2 = c.getNdaysHighLow(crypto=crypto1, days=30)
  print(f"High for {crypto1} - 30 days: ${high2}\n")
  print(f"Low for {crypto1} - 30 days: ${low2}")
  percentage2 = c.round_down(100 * (float(high2.replace(",", "")) / float(low2.replace(",", ""))) - 100)
  print(f"Percentage change: {percentage2} %")
  print("-----------------")




# import CRYPTO as c
# dateprices = c.makeArrayFromCryptoCSV(crypto="SHIB-USD")

def makeArrayFromCryptoCSV(crypto="SHIB-USD"):
  import PlotGRAPHS as p
  # array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
  # p.plotShowArray(array) # [1, 225], [2, 200]
  # +
  # crypto = "SHIB-USD"
  import CRYPTO as c
  l = c.listOfDatesPrices(crypto)
  print(f"going to make x,y from this: len l: {len(l[0])}")
  # print("l:")
  # print(l)
  dateprices = []
  # build the date/price - needed for plotting
  max = len(l[0]) - 1  # count backwards - to put the dates in newest first order
  for i in range(max):
    # date1 = int(l[0][max-i].replace("-",""))
    # string = date1, c.round_down(l[1][i])
    # string = i, c.round_down(l[1][max-i]) #reverse the list with 'max'
    price = l[1][i]
    values = i, price  # c.round_down(l[1][i]) #*100000 shib needs you to add that number - very small ones
    if price < 0.0001:
      values = i, price * 100000  # c.round_down(l[1][i]) #*100000 shib needs you to add that number - very small ones
    dateprices.append(values)
  print(f"dateprices: {dateprices}")
  return dateprices
  # print(f"dateprices[0]: {dateprices[0]}")
  # print(f"dateprices[0][0]: {dateprices[0][0]}")
  # print(f"dateprices[0][1]: {dateprices[0][1]}")


# import CRYPTO as c
# listOfDatesPrices = c.listOfDatesPrices()
#returns 10 rows of date/price info - for ETH - in a list
#getting data out of pandas
def listOfDatesPrices(crypto = "ETH-USD"): #for numpy to plot #- xy is price and date
    import pandas as pd
    import CRYPTO as c
    import time
    import FUNCTIONS as f

    #crypto = "ETH-USD"
    csvUrl = f'crypto-{crypto}--6mo.csv'
    #if file doesn't exist, download the csv for it now
    status = f.fileExists(csvUrl)
    if status==False:
        c.downloadCryptoCSV2(crypto=crypto)
        time.sleep(0.1)
    data = pd.read_csv(csvUrl) #, nrows=10 - limit it to 10 rows
    data2 = data['Date'],data['Close']
    #print(f"data2: {data2}")
    #d0 = data2[0][0] #first entry of the Dates
    #d1 = data2[1][0] #first entry of the Close Price
    #combine columns for matplotlib to plot
    """
    rows = []
    for i in range (len(data2[0])):
        string = f"{data2[0][i]}, {data2[1][i]}"
        rows.append(string)
    #print(f"rows: {rows}")
    """
    var = data2[0], data2[1] #dates, prices
    return var



#listOfDatePrice()







# import CRYPTO as c
# c.downloadStockCSV1(stock="BTC")
# c.downloadStockCSV1(stock="AAPL")

#download the data:
# Download stock data then export as CSV
def downloadStockCSV1(stock="AAPL"):
  import yfinance as yf
  data_df = yf.download(stock, start="2021-06-01", end="2022-02-08")
  data_df.to_csv(f'stocks-{stock}.csv')


# import CRYPTO as c
# c.downloadCryptoCSV2(crypto="ETH-USD")
def downloadCryptoCSV2(crypto="ETH-USD"):
  import yfinance as yf
  data_df = yf.download(tickers=crypto, period='6mo', interval='1d')
  data_df.to_csv(f'crypto-{crypto}--6mo.csv')



# import CRYPTO as c
# c.downloadCryptoCSV2b(crypto="ETH-USD")
def downloadCryptoCSV2b(crypto="ETH-USD"):
  import yfinance as yf
  data_df = yf.download(tickers=crypto, period='30d', interval='30m')
  data_df.to_csv(f'crypto-{crypto}--1mo-30m.csv')


# import CRYPTO as c
# c.downloadCryptoCSV2c(crypto="ETH-USD")
def downloadCryptoCSV2c(crypto="ETH-USD"):
  import yfinance as yf
  data_df = yf.download(tickers=crypto, period='7d', interval='15m')
  data_df.to_csv(f'crypto-{crypto}--7d-15m.csv')




# import CRYPTO as c
# c.downloadCryptoCSV3(crypto="ETH-USD")
def downloadCryptoCSV3(crypto="ETH-USD"): # "DOGE-USD", "BTC-USD"
  import yfinance as yf
  data_df = yf.download(tickers=crypto, start="2021-06-01", end="2022-02-08")
  data_df.to_csv(f'crypto-{crypto}--since-6-2021.csv')

# import CRYPTO as c
# c.getCryptoCSVmultiple()

#use this for comparison later - perhaps
def getCryptoCSVmultiple():
  import yfinance as yf
  df = yf.download(tickers = ["DOGE-USD", "BTC-USD"], start = "2020-01-01", end = "2021-01-01")
  #do something with this
  #return df

#-------------------------


# import CRYPTO as c
# c.getCryptoDATA()

# yfinance
#any interval of data, every 5 minutes, and for how long -for 2 hours
# always up to now
def getCryptoDATA(tickers='BTC-USD'):
  # Data Source
  import yfinance as yf

  # Data viz
  # import plotly.graph_objs as go

  data = yf.download(tickers='BTC-USD', period='2h', interval='5m')

  #data = yf.download(tickers='BTC-USD', period='22h', interval='15m')
  print("data:")
  print(data)
  return data


  """
                                     Open          High  ...     Adj Close    Volume
  Datetime                                               ...                        
  2022-01-29 21:30:00+00:00  38560.468750  38560.468750  ...  38455.457031   2625536
  2022-01-29 21:45:00+00:00  38435.304688  38480.941406  ...  38463.277344  14565376
  """



# import CRYPTO as c
# num = c.round_down(n=1.2345, decimals=2)

#c.round_down()
def round_down(n=1.2345, decimals=2):
  import math
  multiplier = 10 ** decimals
  return math.floor(n * multiplier) / multiplier



# import CRYPTO as c
# num = c.dollars(n=1111.2345)

#formats the number for dollars
def dollars(number):
  number = "{:,}".format(round_down(number))
  return number

# import CRYPTO as c
# high, low = c.getNdaysHighLow(crypto="ETH-USD",days=7)
# high, low = c.getNdaysHighLow(crypto="ETH-USD",days=30)

#need to have downloaded the CSV for this:
#get the highest high for 7 days
def getNdaysHighLow(crypto="ETH-USD",days=7):
  #read the csv file
  import pandas as pd
  csvFilename = f"crypto-{crypto}--6mo.csv"
  daysData = pd.read_csv(csvFilename, index_col='Date')
  #print(f"daysData: {daysData}")
  #print(daysData[['High']]) #only get the highs - #184

  days7 = daysData.tail(days) #get only last 7 days #7
  #print(days7[['High','Low']]) #only get the highs

  columnHigh = days7["High"]
  max_value = columnHigh.max()
  #print(f"max_value: {max_value}")
  columnMin = days7["Low"]
  min_value = columnMin.min()
  #print(f"min_value: {min_value}")
  high = dollars(max_value)
  low = dollars(min_value)
  return high, low


# import CRYPTO as c
# c.getCryptoInfo(cryptoName="BTC",currency="USD") # crypto.getCryptoInfo()

#crypto price and full name
def getCryptoInfo(cryptoName="BTC",currency="USD"):
  import cryptocompare  # pip install cryptocompare

  def get_crypto_price(cryptocurrency, currency):
    return cryptocompare.get_price(cryptocurrency, currency=currency)[cryptocurrency][currency]

  def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

  print(f"{get_crypto_name(cryptoName)} price now: ${get_crypto_price(cryptoName, currency):,}")  # 33089.15
  #print(get_crypto_name(cryptoName))  # Bitcoin (BTC)



# https://github.com/danpaquin/coinbasepro-python


#v1

#import CRYPTO as c #saves the tick data
#c.cryptoGetTICKS() #default is for 'ETH-US'

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

  def ticker2(name="ETH-USD",counter=0):
    o = public_client.get_product_ticker(product_id=name)
    string1Tick = "["+name + "]["+str(counter)+"] " + str(o)
    print(string1Tick)
    saveTickData(string1Tick)
    time.sleep(2)
    return string1Tick


  def ticker(name="ETH-USD"):
    o = public_client.get_product_ticker(product_id=name)
    string1Tick = "["+name + "] " + str(o)
    print(string1Tick)
    saveTickData(string1Tick)
    time.sleep(2)
    return string1Tick

  # ticker('ETH-USD')

  def ticks(n, name):
    for i in range(n):
      ticker2(name,i)

  def saveTickData(string1Tick):
    # Append-adds at last
    file1 = open("crypto_tick_data.txt", "a")  # append mode
    file1.write(f"{string1Tick} \n")
    file1.close()

  #Get 20 Ticks, default is every 2 seconds
  ticks(20, name) # name = 'ETH-USD'
