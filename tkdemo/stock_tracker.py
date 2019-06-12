from tkinter import Tk, Label, Frame, Button, Entry, Canvas, PhotoImage
import bs4 as bs
from pandas.plotting import register_matplotlib_converters
import datetime as dt
import os
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests

#master = Tk()
#master.title('Stock Ticker Tracker')

# def save_sp500_tickers():
#     resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
#     soup = bs.BeautifulSoup(resp.text, "lxml")
#     table = soup.find('table', {'class':'wikitable sortable'})
#     tickers = []
#     for row in table.findAll('tr')[1:]:
#         ticker = row.findAll('td')[0].text
#         tickers.append(ticker)
#     with open("sp500tickers.pickle","wb") as f:
#         pickle.dump(tickers,f)
#     print(tickers[1])
#     return tickers

# def get_data_from_yahoo(reload_sp500=False):
#     if reload_sp500:
#         tickers = save_sp500_tickers()
#     else:
#         with open("sp500tickers.pickle","rb") as f:
#             tickers = pickle.load(f)
#     if not os.path.exists('stock_dfs'):
#         os.makedirs('stock_dfs')
#     start = dt.datetime(2000,1,1)
#     end = dt.datetime(2016,12,31)

#     for ticker in tickers:
#         if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
#             df = web.DataReader(ticker, 'yahoo', start,end)
#             df.to_csv('stock_dfs/{}.csv'.format(ticker))
#         else:
#             print('Already have {} '.format(ticker))
    

register_matplotlib_converters()
style.use('ggplot')

#save_sp500_tickers()
#get_data_from_yahoo()
#Reading CSV File 
#df = pd.read_csv('AMD.csv', parse_dates=True, index_col=0)

#Find 100 Moving Average
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#Print top 5 
#print(df.head())

#Open-high-low-close Data
#df_ohlc = df['Adj Close'].resample('10D').ohlc()
#df_volume = df['Volume'].resample('10D').sum()

#Reset index for ohlc
#df_ohlc.reset_index(inplace=True)

#Convert to mdates
#df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #convert date time object to a mdate number ex.700000

#print(df_ohlc.head())

#Multiple Subplots
#ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
#ax1.xaxis_date()

#Create candlestick chart, axis, data, width = thickness of candle, colorup = color of candlestick going up
#candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

#ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
#ax1.plot(df.index, df['Adj Close'])
#ax1.plot(df.index, df['100ma'])
#ax2.bar(df.index, df['Volume'])

#plt.show()






start = dt.datetime.today().strftime('%Y-%m-%d')
end = dt.datetime.today().strftime('%Y-%m-%d')
df = web.DataReader('AMD','yahoo', start,end)
df.to_csv('AMD.csv')               
#print(df[['High']])
#df['Adj Close'].plot()
#plt.show()
#df.dropna(inplace=True)
#print(df[['Open','High']].tail(50))