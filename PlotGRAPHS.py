#plot graphs and see them as images or live


#import PlotGRAPHS as p
#p.plotCSVcryptoMatplot(crypto="ETH-USD")
#p.plotCSVcryptoMatplot(crypto="ADA-USD")
#p.plotCSVcryptoMatplot(crypto="SHIB-USD")
#p.plotCSVcryptoMatplot(crypto="BTC-USD")
#--------------
#p.plotCSVcrypto1matplotlibShow() # candlesticks
#plot.crytpoPlot1matplotlibShow() #see 7 graphs of 7 cryptos



# import PlotGRAPHS as p
# p.plotCSVcrypto1matplotlibShow() # candlesticks - loads git AAPL stock
# p.crytpoPlot1matplotlibShow() # see 7 graphs of 7 cryptos
#
# p.plotCSVcandlesticks2web() # loads git AAPL stock
#
# p.barChart1() # super simple example
#
# p.plotPointsTkinter() # blue dots - and red color x's
# import PlotGRAPHS as plot
# p.crytpoCandlestickPlot2web()
# p.crytpoCandlestickPlot1web()
# p.crytpoLivePlot1() #doesn't work
# p.coolTerminalTextOutput()



#---------------------------------------------


# import PlotGRAPHS as p
# p.singlePlot()

# p.doublePlot1()
# p.doublePlot2()
# p.doublePlot3()
# p.doublePlot4()
# p.doublePlot5()
# p.doublePlot6()
# p.doublePlot7()
# p.doublePlot8()

# p.plotManualXY1()
# p.plotManualXY2()
# p.plotManualXY3()
# listOfDatesPrices = p.listOfDatesPrices()

# p.plotManualXY4()

# import PlotGRAPHS as p
#array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
#p.plotShowArray(array) # [1, 225], [2, 200]
#+
## listOfDatesPrices = p.listOfDatesPrices()


# import PlotGRAPHS as p
# p.showNiceCryptoView("SHIB-USD")

def showNiceCryptoView(crypto = "SHIB-USD"):
    # show 4 on one board
    import CRYPTO as c
    import PlotGRAPHS as p
    dateprices = c.makeArrayFromCryptoCSV(crypto=crypto)
    p.plotShow3(dateprices, crypto=crypto)


# import PlotGRAPHS as p
# p.showCrypto("SHIB-USD")
def showCrypto(crypto = "SHIB-USD", days=0):
    cryptoName = crypto
    import CRYPTO as c
    import PlotGRAPHS as p
    datePricesArray = c.makeArrayFromCryptoCSV(cryptoName)
    #select only 30 to plot
    if days==0:
        someDays = datePricesArray
        print(f"days: {days}")
    elif days>0:
        #extract the number of days - as rows from the array
        someDays = datePricesArray[:days]
        print(f"days: {days}")

    p.plotShowArray(someDays,cryptoName) # [1, 225], [2, 200]



# import PlotGRAPHS as p
#array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
#p.plotShowArray(array) # [1, 225], [2, 200]

def plotShowArray(array,crypto="ETH-USD"): # [1, 225], [2, 200]
    import numpy as np
    from matplotlib import pyplot as plt

    #array = [1, 225], [2, 200]
    # array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
    data = np.array(array)
    x, y = data.T
    plt.plot(x, y)
    #extra - not needed
    plt.title(crypto)
    plt.xlabel('Days - Date ... (30 = 1month)')
    plt.ylabel('Price')
    plt.show()



#show 2 on one board
#import CRYPTO as c
#import PlotGRAPHS as p
#dateprices = c.makeArrayFromCryptoCSV(crypto="ETH-USD")
#p.plotShow2(dateprices, crypto="ETH-USD")

def plotShow2(array, crypto="ETH-USD"):  # [1, 225], [2, 200]
    import numpy as np
    from matplotlib import pyplot as plt

    # array = [1, 225], [2, 200]
    # array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
    data = np.array(array)
    x, y = data.T
    data1 = np.array(array[:90])
    x1, y1 = data1.T
    # data2 = np.array(array[:60])
    # data3 = np.array(array[:30])
    fig, axs = plt.subplots(2)  # SHOW plt.show()
    fig.suptitle(crypto)
    axs[0].plot(x, y)  # access the 2 plots with axs[], I think
    axs[1].plot(x1, y1)

    # extra - not needed
    #plt.title(crypto)
    plt.xlabel('Days - Date ... (30 = 1month)')
    plt.ylabel('Price')
    plt.show()




# import PlotGRAPHS as p
# p.doublePlot7a()

#plotting with COLORS
#opens 2 figure windows
def doublePlot7a():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    #each figure you make will be displayed in its own window
    # this opens 2 figure windows
    #
    #making figure 1
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x + 1, -y, 'tab:green')
    ax4.plot(x + 2, -y ** 2, 'tab:red')

    #making figure 2
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x + 1, -y, 'tab:green')
    ax4.plot(x + 2, -y ** 2, 'tab:red')


    plt.show()


#doublePlot7()



#show 2 on one board
#import CRYPTO as c
#import PlotGRAPHS as p
#dateprices = c.makeArrayFromCryptoCSV(crypto="ETH-USD")
#p.plotShow3(dateprices, crypto="ETH-USD")

def plotShow3(array, crypto="ETH-USD"):  # [1, 225], [2, 200]
    import numpy as np
    from matplotlib import pyplot as plt

    # array = [1, 225], [2, 200]
    # array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
    data = np.array(array)
    x, y = data.T
    array.sort(reverse=True)
    data1 = np.array(array[:30]) # this gives 1st 60 days - from the left
    x1, y1 = data1.T
    data2 = np.array(array[:60]) # this removes 120 days - from the left
    x2, y2 = data2.T
    data3 = np.array(array[:90]) # this gives last 60 days - from the right #ledgend is messed up - it says 180
    x3, y3 = data3.T

    fig, axs = plt.subplots(4)  # SHOW plt.show()
    fig.suptitle(f'{crypto} - 6 months, 90 days, 60 days, 30 days')
    axs[0].plot(x, y)  # access the 2 plots with axs[], I think
    axs[1].plot(x3, y3)
    axs[2].plot(x2, y2)
    axs[3].plot(x1, y1)

    # extra - not needed
    #plt.title(crypto)
    plt.xlabel('Days - Date ... (30 = 1month)')
    plt.ylabel('Price')
    plt.show()





#-----------------------------------

#plot 2 together

# import PlotGRAPHS as p
# p.singlePlot()

def singlePlot():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, ax = plt.subplots() #SHOW plt.show()
    ax.plot(x, y)
    ax.set_title('A single plot')

    plt.show()



# import PlotGRAPHS as p
# p.doublePlot1()

def doublePlot1():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, axs = plt.subplots(2) #SHOW plt.show()
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(x, y) #access the 2 plots with axs[], I think
    axs[1].plot(x, -y)

    plt.show()

#doublePlot1()




# import PlotGRAPHS as p
# p.doublePlot2()

def doublePlot2():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, (ax1, ax2) = plt.subplots(1, 2) # SHOW plt.show()
    fig.suptitle('Horizontally stacked subplots')
    ax1.plot(x, y)
    ax2.plot(x, -y)

    plt.show()

#doublePlot2()



# import PlotGRAPHS as p
# p.doublePlot3()

#4 up together
def doublePlot3():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, axs = plt.subplots(2, 2)
    fig.suptitle('4 UP - stacked subplots')
    axs[0, 0].plot(x, y)
    axs[0, 0].set_title('Axis [0, 0]')
    axs[0, 1].plot(x, y, 'tab:orange')
    axs[0, 1].set_title('Axis [0, 1]')
    axs[1, 0].plot(x, -y, 'tab:green')
    axs[1, 0].set_title('Axis [1, 0]')
    axs[1, 1].plot(x, -y, 'tab:red')
    axs[1, 1].set_title('Axis [1, 1]')

    for ax in axs.flat:
        ax.set(xlabel='x-label', ylabel='y-label')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()

#doublePlot3()





# import PlotGRAPHS as p
# p.doublePlot4()

#4 up together
def doublePlot4():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Sharing x per column, y per row ... 4 UP - stacked subplots')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x, -y, 'tab:green')
    ax4.plot(x, -y ** 2, 'tab:red')

    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()

#doublePlot4()


# import PlotGRAPHS as p
# p.doublePlot5()

#4 up together
def doublePlot5():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, (ax1, ax2) = plt.subplots(2) #PLOT TO SHOW
    fig.suptitle('Axes values are scaled individually by default - 4 UP - stacked subplots')
    ax1.plot(x, y)
    ax2.plot(x + 1, -y)

    plt.show()


#doublePlot5()



# import PlotGRAPHS as p
# p.doublePlot6()

#plot with characters '+'
def doublePlot6():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, axs = plt.subplots(3, sharex=True, sharey=True)
    fig.suptitle('Sharing both axes - sharex=True, sharey=True')
    axs[0].plot(x, y ** 2)
    axs[1].plot(x, 0.3 * y, 'o')
    axs[2].plot(x, y, '+')

    plt.show()


#doublePlot6()



# import PlotGRAPHS as p
# p.doublePlot7()

#plotting with COLORS
#opens 2 figure windows
def doublePlot7():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    #each figure you make will be displayed in its own window
    # this opens 2 figure windows
    #
    #making figure 1
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x + 1, -y, 'tab:green')
    ax4.plot(x + 2, -y ** 2, 'tab:red')

    #making figure 2
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x + 1, -y, 'tab:green')
    ax4.plot(x + 2, -y ** 2, 'tab:red')


    plt.show()


#doublePlot7()



# import PlotGRAPHS as p
# p.doublePlot8()

# plotting with COLORS
# opens 2 figure windows
def doublePlot8():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    # x = np.linspace(0, 2 * np.pi, 400)
    # y = np.sin(x ** 2)

    x = np.array([100, 200, 300, 250, 350])
    y = np.array([1, 2, 3, 4, 5])

    # each figure you make will be displayed in its own window
    # this opens 2 figure windows
    #
    # making figure 1
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    ax1 = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    #ax2.plot(x, y ** 2, 'tab:orange')
    #ax3.plot(x + 1, -y, 'tab:green')
    #ax4.plot(x + 2, -y ** 2, 'tab:red')


    plt.show()


#doublePlot8()



# import PlotGRAPHS as p
# p.plotManualXY1()

def plotManualXY1():
    import numpy as np
    from matplotlib import pyplot as plt

    array = [
        [1, 225],
        [2, 200],
        [3, 300],
        [4, 250],
        [5, 350],
    ]
    data = np.array(array)
    x, y = data.T
    plt.plot(x,y)
    plt.show()

#plotManualXY1()



# import PlotGRAPHS as p
# p.plotManualXY2()

#smallest plot - 2 points
def plotManualXY2():
    import numpy as np
    from matplotlib import pyplot as plt

    array = [1, 225], [2, 200]#, [3, 300], [4, 250], [5, 350]
    #data = np.array(array)
    #data = np.array([1, 225])
    data = np.array(array)
    x, y = data.T
    plt.plot(x,y)
    plt.show()

#plotManualXY2()



# import PlotGRAPHS as p
# p.plotManualXY3()

#smallest plot - 2 points
def plotManualXY3():
    import numpy as np
    from matplotlib import pyplot as plt

    array = [1, 225], [2, 200]
    #array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
    #data = np.array(array)
    #data = np.array([1, 225])
    data = np.array(array)
    x, y = data.T
    plt.plot(x,y)
    plt.show()

#plotManualXY3()








# import PlotGRAPHS as p
# p.plotManualXY4()

def plotManualXY4():
    import matplotlib.pyplot as plt
    import numpy as np

    # X axis parameter:
    xaxis = np.array([2, 4, 9])

    # Y axis parameter:
    yaxis = np.array([2, 4, 9])

    plt.plot(xaxis, yaxis)
    plt.show()

#plotManualXY5()






#-------------------------------

# import PlotGRAPHS as p
# p.plotCSVcryptoMatplot3(crypto="ETH-USD") #load other csv files

# matplotlib
def plotCSVcryptoMatplot3(crypto="ETH-USD"): #30*6
    # python_candlestick_chart.py

    import matplotlib.pyplot as plt
    from mplfinance.original_flavor import candlestick_ohlc
    import pandas as pd
    import matplotlib.dates as mpl_dates
    import CRYPTO as c
    import FUNCTIONS as f
    import time

    plt.style.use('ggplot')

    # Extracting Data for plotting
    #csvUrl = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    csvUrl = f'crypto-{crypto}--7d-15m.csv'
    #if file doesn't exist, download the csv for it now
    status = f.fileExists(csvUrl)
    if status==False:
        c.downloadCryptoCSV2(crypto=crypto)
        time.sleep(0.1)
    data = pd.read_csv(csvUrl, nrows=350) # , nrows=700
    ohlc = data.loc[:, ['Datetime', 'Open', 'High', 'Low', 'Close']]
    ohlc['Datetime'] = pd.to_datetime(ohlc['Datetime'])
    ohlc['Datetime'] = ohlc['Datetime'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)

    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

    # Setting labels & titles
    ax.set_xlabel('Datetime')
    ax.set_ylabel('Price')
    fig.suptitle(f'Daily Candlestick Chart of {crypto}')

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()



#-------------------------------

# import PlotGRAPHS as p
# p.plotCSVcryptoMatplot2(crypto="ETH-USD") #load other csv files

# matplotlib - opens so you can see it
# it downloads the file if it doesn't have it yet
def plotCSVcryptoMatplot2(crypto="ETH-USD", plotQty=30): #30*6
    # python_candlestick_chart.py

    import matplotlib.pyplot as plt
    from mplfinance.original_flavor import candlestick_ohlc
    import pandas as pd
    import matplotlib.dates as mpl_dates
    import CRYPTO as c
    import FUNCTIONS as f
    import time

    plt.style.use('ggplot')

    # Extracting Data for plotting
    #csvUrl = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    csvUrl = f'crypto-{crypto}--6mo.csv'
    #if file doesn't exist, download the csv for it now
    status = f.fileExists(csvUrl)
    if status==False:
        c.downloadCryptoCSV2(crypto=crypto)
        time.sleep(0.1)
    data = pd.read_csv(csvUrl, nrows=plotQty) #, skiprows=30, nrows=30 # plotQty
    #data.reindex(index=data.index[::-1]) #get them in the right date order


    ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    ohlc['Date'] = pd.to_datetime(ohlc['Date'])
    ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)

    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle(f'Daily Candlestick Chart of {crypto}')

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()





# import PlotGRAPHS as p
# p.plotCSVcryptoMatplot1(crypto="ETH-USD") #load other csv files

# matplotlib - opens so you can see it
# it downloads the file if it doesn't have it yet
def plotCSVcryptoMatplot1(crypto="ETH-USD"): # candlesticks
    # python_candlestick_chart.py

    import matplotlib.pyplot as plt
    from mplfinance.original_flavor import candlestick_ohlc
    import pandas as pd
    import matplotlib.dates as mpl_dates
    import CRYPTO as c
    import FUNCTIONS as f
    import time

    plt.style.use('ggplot')

    # Extracting Data for plotting
    #csvUrl = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    csvUrl = f'crypto-{crypto}--6mo.csv'
    #if file doesn't exist, download the csv for it now
    status = f.fileExists(csvUrl)
    if status==False:
        c.downloadCryptoCSV2(crypto=crypto)
        time.sleep(0.1)
    data = pd.read_csv(csvUrl)
    ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
    ohlc['Date'] = pd.to_datetime(ohlc['Date'])
    ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)

    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle(f'Daily Candlestick Chart of {crypto}')

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()





# import PlotGRAPHS as plot
# plot.crytpoPlot1matplotlibShow()

#see 7 graphs of 7 cryptos
def crytpoPlot1matplotlibShow():
    import pandas_datareader as web  # pip install pandas_datareader
    import matplotlib.pyplot as plt
    import mplfinance as mpf  # pip install mplfinance
    import seaborn as sns  # pip install seaborn
    import datetime as dt

    currency = "USD"
    metric = "Close"

    start = dt.datetime(2018, 1, 1)
    end = dt.datetime.now()

    crypto = ['BTC', 'ETH', 'LTC', 'XRP', 'DASH', 'SC']
    colnames = []

    first = True

    for ticker in crypto:
        data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
        if first:
            combined = data[[metric]].copy()
            colnames.append(ticker)
            combined.columns = colnames
            first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

    plt.yscale('log')

    for ticker in crypto:
        plt.plot(combined[ticker], label=ticker)

    plt.legend(loc="upper right")

    plt.show()





# import PlotGRAPHS as p
# p.plotCSVcrypto1matplotlibShow() #candlesticks

# matplotlib - opens so you can see it
def plotCSVcrypto1matplotlibShow(): # candlesticks
    # python_candlestick_chart.py

    import matplotlib.pyplot as plt
    from mplfinance.original_flavor import candlestick_ohlc
    import pandas as pd
    import matplotlib.dates as mpl_dates

    plt.style.use('ggplot')

    # Extracting Data for plotting
    csvUrl = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    #csvUrl = 'crypto-ETH-USD--6mo.csv'
    data = pd.read_csv(csvUrl)
    ohlc = data.loc[:, ['Date', 'AAPL.Open', 'AAPL.High', 'AAPL.Low', 'AAPL.Close']]
    ohlc['Date'] = pd.to_datetime(ohlc['Date'])
    ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
    ohlc = ohlc.astype(float)

    # Creating Subplots
    fig, ax = plt.subplots()

    candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

    # Setting labels & titles
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    fig.suptitle('Daily Candlestick Chart of AAPL')

    # Formatting Date
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()

    fig.tight_layout()

    plt.show()








# import PlotGRAPHS as p
# p.plotCSVcandlesticks2web() # loads git AAPL stock

# opens webpage to see it
def plotCSVcandlesticks2web():
    import plotly.graph_objects as go
    import pandas as pd

    csvUrl = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
    df = pd.read_csv(csvUrl)

    fig = go.Figure(data=go.Ohlc(x=df['Date'],
                                 open=df['AAPL.Open'],
                                 high=df['AAPL.High'],
                                 low=df['AAPL.Low'],
                                 close=df['AAPL.Close']))
    fig.update_layout(title_text='AAPL For Several Years', title_x=0.5)
    fig.show()


#-----------------------

# import PlotGRAPHS as plot
# plot.barChart1() # super simple example

def barChart1():
    import matplotlib.pyplot as plt
    names = ['a', 'b', 'c']
    values = [1, 10, 100]
    plt.figure(1, figsize=(9, 3))
    plt.bar(names, values)
    plt.show()

#barChart1()


#--------------------------


# import PlotGRAPHS as plot
# plot.plotPointsTkinter() # matplotlib # blue dots - and red color x's

#blue dots - and red color x's
# matplotlib in Tkinter
from tkinter import * #this must be outside the function
def plotPointsTkinter(): # matplotlib
    # Import required libraries
    # from tkinter import *
    from tkinter import ttk
    import matplotlib
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    # Create an instance of tkinter frame
    win= Tk()

    # Set the window size
    win.geometry("700x350")

    # Use TkAgg
    matplotlib.use("TkAgg")

    # Create a figure of specific SIZE
    figure = Figure(figsize=(7, 3.45), dpi=100)

    # Define the points for plotting the figure
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(0.5, 0.3, color="blue", marker="o", linestyle="")
    plot.plot(1, 0.8, color="blue", marker="o", linestyle="")

    # Define Data points for x and y axis
    x = [ 0.2, 0.5, 0.8, 1.0 ]
    y = [ 1.0, 1.2, 1.3, 1.4 ]
    plot.plot(x, y, color="red", marker="x", linestyle="")

    # Add a canvas widget to associate the figure with canvas
    canvas = FigureCanvasTkAgg(figure, win)
    canvas.get_tk_widget().grid(row=0, column=0)

    win.mainloop()




#------------------------------------------




# import PlotGRAPHS as plot
# plot.crytpoCandlestickPlot2web()

# opens browser and presents you with the candlestick graph of BTC
# http://127.0.0.1:63548/ #uses Plotly

# The Correlation between Different Cryptocurrencies, 'BTC', 'ETH', 'LTC', 'XRP'
def crytpoCandlestickPlot2web():
    from datetime import datetime, timedelta

    import pandas as pd
    import pandas_datareader as pdr
    import plotly.graph_objects as go

    CRYPTOS = ['BTC', 'ETH', 'LTC', 'XRP']    # CRYPTO = 'BTC'
    CURRENCY = 'USD'

    def getData(cryptocurrency):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        last_year_date = (now - timedelta(days=365)).strftime("%Y-%m-%d")

        start = pd.to_datetime(last_year_date)
        end = pd.to_datetime(current_date)

        data = pdr.get_data_yahoo(f'{cryptocurrency}-{CURRENCY}', start, end)

        return data

    # if __name__ == '__main__':
    # crypto_data = getData(CRYPTO)

    crypto_data = {crypto: getData(crypto) for crypto in CRYPTOS}

    # crypto_data = dict()
    # for crypto in CRYPTOS:
    #     crypto_data[crypto] = getData(crypto)



    # Candlestick
    fig = go.Figure()

    # Scatter
    for idx, name in enumerate(crypto_data):
        fig = fig.add_trace(
            go.Scatter(
                x=crypto_data[name].index,
                y=crypto_data[name].Close,
                name=name,
            )
        )

    fig.update_layout(
        title='The Correlation between Different Cryptocurrencies',
        xaxis_title='Date',
        yaxis_title=f'Closing price ({CURRENCY})',
        legend_title='Cryptocurrencies'
    )
    fig.update_yaxes(type='log', tickprefix='$')

    fig.show()




# import PlotGRAPHS as plot
# plot.crytpoCandlestickPlot1web()

# opens browser and presents you with the candlestick graph of BTC
# http://127.0.0.1:63548/
def crytpoCandlestickPlot1web():
    from datetime import datetime, timedelta

    import pandas as pd
    import pandas_datareader as pdr
    import plotly.graph_objects as go

    CRYPTO = 'BTC'
    CURRENCY = 'USD'

    def getData(cryptocurrency):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        last_year_date = (now - timedelta(days=365)).strftime("%Y-%m-%d")

        start = pd.to_datetime(last_year_date)
        end = pd.to_datetime(current_date)

        data = pdr.get_data_yahoo(f'{cryptocurrency}-{CURRENCY}', start, end)

        return data

    # if __name__ == '__main__':
    crypto_data = getData(CRYPTO)

    # Candlestick
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=crypto_data.index,
                open=crypto_data.Open,
                high=crypto_data.High,
                low=crypto_data.Low,
                close=crypto_data.Close
            ),
            go.Scatter(
                x=crypto_data.index,
                y=crypto_data.Close.rolling(window=20).mean(),
                mode='lines',
                name='20SMA',
                line={'color': '#ff006a'}
            ),
            go.Scatter(
                x=crypto_data.index,
                y=crypto_data.Close.rolling(window=50).mean(),
                mode='lines',
                name='50SMA',
                line={'color': '#1900ff'}
            )
        ]
    )

    fig.update_layout(
        title=f'The Candlestick graph for {CRYPTO}',
        xaxis_title='Date',
        yaxis_title=f'Price ({CURRENCY})',
        xaxis_rangeslider_visible=False
    )
    fig.update_yaxes(tickprefix='$')

    fig.show()



# import PlotGRAPHS as plot
# plot.crytpoLivePlot1()

def crytpoLivePlot1():
    import cryptocompare #pip install cryptocompare

    def get_crypto_price(cryptocurrency, currency):
        return cryptocompare.get_price(cryptocurrency, curr=currency)[cryptocurrency][currency]

    def get_crypto_name(cryptocurrency):
        return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

    print(get_crypto_price('BTC', 'USD'))  # 33089.15
    print(get_crypto_name('ETH'))  # Etherium (ETH)

    # -------------

    import matplotlib.pyplot as plt
    from datetime import datetime
    from matplotlib.animation import FuncAnimation

    # set style better visualize the live plot
    plt.style.use('seaborn')

    # x: datetime objects, y: price
    x_vals = []
    y_vals = []

    # animate function
    def animate(i):
        x_vals.append(datetime.now())
        y_vals.append(get_crypto_price('BTC', 'USD'))

        # specify plot title
        plt.title(get_crypto_name('BTC') + ' Price Live Plotting')

        plt.xlabel('Date')
        plt.ylabel('Price (USD$)')

        # actual plotting
        plt.plot_date(x_vals, y_vals, linestyle="solid", ms=0)

        plt.tight_layout()

    # call animate function and specify update time
    ani = FuncAnimation(plt.gcr(), animate, interval=1000)

    # show plot
    plt.show()






# import PlotGRAPHS as plot
# plot.coolGUIOutput4()

def coolGUIOutput4():
    import tkinter as tk
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    def cents_different(x, y):
        if x >= y:
            result = x - y
        else:
            result = (y - x) * (-1)
        return result

    # convert prices to percentages
    prices = [2575.56, 2576.85, 2577.06, 2576.74, 2577.53, 2577.08, 2577.63, 2576.73, 2576.44, 2576.94, 2576.47,
              2577.09,
              2577.62, 2576.7, 2576.62, 2577.79, 2578.12, 2577.51, 2577.6, 2576.28]
    cents_changed = []
    percentages = []
    for i in range(len(prices)):
        if (i == 0):
            lastPrice = prices[i]
            thisPrice = prices[i]
        else:
            lastPrice = prices[i - 1]
            thisPrice = prices[i]
        cents = cents_different(lastPrice, thisPrice)
        cents_changed.append(cents)

        percentageMove = lastPrice / thisPrice  # % move up or down - from previous price
        print(
            f"lastPrice: {lastPrice}, thisPrice: {thisPrice} ... cents: {cents:.2f} ... percentageMove: {percentageMove} ")
        percentages.append(percentageMove)  # divided by the last one




    data2 = {'Second': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ],
             'CentsChanged': cents_changed
             }
    df2 = DataFrame(data2, columns=['Second', 'CentsChanged'])

    root = tk.Tk()


    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Second', 'CentsChanged']].groupby('Second').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Second Vs. Crypto Price (in cents)')


    root.mainloop()





# import PlotGRAPHS as plot
# plot.coolGUIOutput3()

def coolGUIOutput3():
    import tkinter as tk
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    data2 = {'Second': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 ],
             'CryptoPrice': [2575.56, 2576.85, 2577.06, 2576.74, 2577.53, 2577.08, 2577.63, 2576.73, 2576.44, 2576.94, 2576.47, 2577.09, 2577.62, 2576.7, 2576.62, 2577.79, 2578.12, 2577.51, 2577.6, 2576.28 ]
             }
    df2 = DataFrame(data2, columns=['Second', 'CryptoPrice'])

    root = tk.Tk()


    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Second', 'CryptoPrice']].groupby('Second').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Second Vs. Crypto Price')


    root.mainloop()




# import PlotGRAPHS as plot
# plot.coolGUIOutput2()

def coolGUIOutput2():
    import tkinter as tk
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


    data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
             'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
             }
    df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])

    root = tk.Tk()


    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate')


    root.mainloop()



# import PlotGRAPHS as plot
# plot.coolGUIOutput()

def coolGUIOutput():
    import tkinter as tk
    from pandas import DataFrame
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
             'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
             }
    df1 = DataFrame(data1, columns=['Country', 'GDP_Per_Capita'])

    data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
             'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
             }
    df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])

    data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
             'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
             }
    df3 = DataFrame(data3, columns=['Interest_Rate', 'Stock_Index_Price'])

    root = tk.Tk()

    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Country Vs. GDP Per Capita')

    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate')

    figure3 = plt.Figure(figsize=(5, 4), dpi=100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Interest_Rate'], df3['Stock_Index_Price'], color='g')
    scatter3 = FigureCanvasTkAgg(figure3, root)
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax3.legend(['Stock_Index_Price'])
    ax3.set_xlabel('Interest Rate')
    ax3.set_title('Interest Rate Vs. Stock Index Price')

    root.mainloop()


# import PlotGRAPHS as plot
# plot.coolTerminalTextOutput()

def coolTerminalTextOutput():
  from pandas import DataFrame

  data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
           'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]
           }
  df1 = DataFrame(data1, columns=['Country', 'GDP_Per_Capita'])
  print(df1)

  data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
           'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
           }
  df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])
  print(df2)

  data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
           'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
           }
  df3 = DataFrame(data3, columns=['Interest_Rate', 'Stock_Index_Price'])
  print(df3)





# import PlotGRAPHS as p
# p.singlePlot()

# p.doublePlot1()
# p.doublePlot2()
# p.doublePlot3()
# p.doublePlot4()
# p.doublePlot5()
# p.doublePlot6()
# p.doublePlot7()
# p.doublePlot8()

# p.plotManualXY1()
# p.plotManualXY2()
# p.plotManualXY3()
# listOfDatesPrices = p.listOfDatesPrices()

# p.plotManualXY4()






#plot 2 together

# import PlotGRAPHS as p
# p.singlePlot()

def singlePlot():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, ax = plt.subplots() #SHOW plt.show()
    ax.plot(x, y)
    ax.set_title('A single plot')

    plt.show()



# import PlotGRAPHS as p
# p.doublePlot1()

def doublePlot1():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, axs = plt.subplots(2) #SHOW plt.show()
    fig.suptitle('Vertically stacked subplots')
    axs[0].plot(x, y) #access the 2 plots with axs[], I think
    axs[1].plot(x, -y)

    plt.show()

#doublePlot1()




# import PlotGRAPHS as p
# p.doublePlot2()

def doublePlot2():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, (ax1, ax2) = plt.subplots(1, 2) # SHOW plt.show()
    fig.suptitle('Horizontally stacked subplots')
    ax1.plot(x, y)
    ax2.plot(x, -y)

    plt.show()

#doublePlot2()



# import PlotGRAPHS as p
# p.doublePlot3()

#4 up together
def doublePlot3():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, axs = plt.subplots(2, 2)
    fig.suptitle('4 UP - stacked subplots')
    axs[0, 0].plot(x, y)
    axs[0, 0].set_title('Axis [0, 0]')
    axs[0, 1].plot(x, y, 'tab:orange')
    axs[0, 1].set_title('Axis [0, 1]')
    axs[1, 0].plot(x, -y, 'tab:green')
    axs[1, 0].set_title('Axis [1, 0]')
    axs[1, 1].plot(x, -y, 'tab:red')
    axs[1, 1].set_title('Axis [1, 1]')

    for ax in axs.flat:
        ax.set(xlabel='x-label', ylabel='y-label')

    # Hide x labels and tick labels for top plots and y ticks for right plots.
    for ax in axs.flat:
        ax.label_outer()

    plt.show()

#doublePlot3()





# import PlotGRAPHS as p
# p.doublePlot4()

#4 up together
def doublePlot4():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Sharing x per column, y per row ... 4 UP - stacked subplots')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x, -y, 'tab:green')
    ax4.plot(x, -y ** 2, 'tab:red')

    for ax in fig.get_axes():
        ax.label_outer()

    plt.show()

#doublePlot4()


# import PlotGRAPHS as p
# p.doublePlot5()

#4 up together
def doublePlot5():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, (ax1, ax2) = plt.subplots(2) #PLOT TO SHOW
    fig.suptitle('Axes values are scaled individually by default - 4 UP - stacked subplots')
    ax1.plot(x, y)
    ax2.plot(x + 1, -y)

    plt.show()


#doublePlot5()



# import PlotGRAPHS as p
# p.doublePlot6()

#plot with characters '+'
def doublePlot6():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    fig, axs = plt.subplots(3, sharex=True, sharey=True)
    fig.suptitle('Sharing both axes - sharex=True, sharey=True')
    axs[0].plot(x, y ** 2)
    axs[1].plot(x, 0.3 * y, 'o')
    axs[2].plot(x, y, '+')

    plt.show()


#doublePlot6()



# import PlotGRAPHS as p
# p.doublePlot7()

#plotting with COLORS
#opens 2 figure windows
def doublePlot7():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    x = np.linspace(0, 2 * np.pi, 400)
    y = np.sin(x ** 2)

    #each figure you make will be displayed in its own window
    # this opens 2 figure windows
    #
    #making figure 1
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x + 1, -y, 'tab:green')
    ax4.plot(x + 2, -y ** 2, 'tab:red')

    #making figure 2
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    ax2.plot(x, y ** 2, 'tab:orange')
    ax3.plot(x + 1, -y, 'tab:green')
    ax4.plot(x + 2, -y ** 2, 'tab:red')


    plt.show()


#doublePlot7()



# import PlotGRAPHS as p
# p.doublePlot8()

# plotting with COLORS
# opens 2 figure windows
def doublePlot8():
    import matplotlib.pyplot as plt
    import numpy as np

    # Some example data to display
    # x = np.linspace(0, 2 * np.pi, 400)
    # y = np.sin(x ** 2)

    x = np.array([100, 200, 300, 250, 350])
    y = np.array([1, 2, 3, 4, 5])

    # each figure you make will be displayed in its own window
    # this opens 2 figure windows
    #
    # making figure 1
    fig = plt.figure()
    gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
    ax1 = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('Sharing x per column, y per row')
    ax1.plot(x, y)
    #ax2.plot(x, y ** 2, 'tab:orange')
    #ax3.plot(x + 1, -y, 'tab:green')
    #ax4.plot(x + 2, -y ** 2, 'tab:red')


    plt.show()


#doublePlot8()



# import PlotGRAPHS as p
# p.plotManualXY1()

def plotManualXY1():
    import numpy as np
    from matplotlib import pyplot as plt

    array = [
        [1, 225],
        [2, 200],
        [3, 300],
        [4, 250],
        [5, 350],
    ]
    data = np.array(array)
    x, y = data.T
    plt.plot(x,y)
    plt.show()

#plotManualXY1()



# import PlotGRAPHS as p
# p.plotManualXY2()

#smallest plot - 2 points
def plotManualXY2():
    import numpy as np
    from matplotlib import pyplot as plt

    array = [1, 225], [2, 200]#, [3, 300], [4, 250], [5, 350]
    #data = np.array(array)
    #data = np.array([1, 225])
    data = np.array(array)
    x, y = data.T
    plt.plot(x,y)
    plt.show()

#plotManualXY2()



# import PlotGRAPHS as p
# p.plotManualXY3()

#smallest plot - 2 points
def plotManualXY3():
    import numpy as np
    from matplotlib import pyplot as plt

    array = [1, 225], [2, 200]
    #array = [1, 225], [2, 200], [3, 300], [4, 250], [5, 350]
    #data = np.array(array)
    #data = np.array([1, 225])
    data = np.array(array)
    x, y = data.T
    plt.plot(x,y)
    plt.show()

#plotManualXY3()






# import PlotGRAPHS as p
# listOfDatesPrices = p.listOfDatesPrices()
#returns 10 rows of date/price info - for ETH - in a list
#getting data out of pandas
def listOfDatesPrices(crypto="ETH-USD"): #for numpy to plot #- xy is price and date
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
    data = pd.read_csv(csvUrl, nrows=10) #limit it to 10 rows
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


# import PlotGRAPHS as p
# p.plotManualXY4()

def plotManualXY4():
    import matplotlib.pyplot as plt
    import numpy as np

    # X axis parameter:
    xaxis = np.array([2, 4, 9])

    # Y axis parameter:
    yaxis = np.array([2, 4, 9])

    plt.plot(xaxis, yaxis)
    plt.show()

#plotManualXY5()



