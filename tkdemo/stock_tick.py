from tkinter import *
import tkinter as tk
import bs4 as bs
from pandas.plotting import register_matplotlib_converters
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
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

register_matplotlib_converters()
style.use('ggplot')

master = Tk()
master.geometry("600x600")
master.title("STOCK-IT")
master.resizable(width="FALSE", height="FALSE")
 
 
def findStock():
    #stock_symbol_entered = stock_symbol_input.get()
    start = dt.datetime.today().strftime('%Y-%m-%d')
    end = dt.datetime.today().strftime('%Y-%m-%d')
    df = web.DataReader(stock_symbol_input.get().upper(),'yahoo',start,end)
    df.reset_index(inplace=True,drop=False)
    stock_symbol.config(text=stock_symbol_input.get().upper())
    stock_date.config(text=start)
    stock_open.config(text= "$" + str(round(df['Open'][0],2)))
    stock_high.config(text="$" + str(round(df['High'][0],2)))
    stock_low.config(text= "$" + str(round(df['Low'][0],2)))
    stock_close.config(text="$" + str(round(df['Close'][0],2)))
    stock_volume.config(text=str(round(df['Volume'][0],2)))
    stock_adj_close.config(text="$" + str(round(df['Adj Close'][0],2)))


#STOCK SYMBOL LABEL
stock_symbol = Label(master,text="--", font='Montserrat 12')
stock_symbol.grid(column=1,row=2)
 
#STOCK DATE LABEL
stock_date = Label(master,text="--", font='Montserrat 12')
stock_date.grid(column=1,row=3)

#STOCK OPEN LABEL
stock_open = Label(master,text="--", font='Montserrat 12')
stock_open.grid(column=1,row=4)

#STOCK HIGH LABEL
stock_high = Label(master,text="--", font='Montserrat 12')
stock_high.grid(column=1,row=5)

#STOCK LOW LABEL
stock_low = Label(master,text="--", font='Montserrat 12')
stock_low.grid(column=1,row=6)

#STOCK CLOSE LABEL
stock_close = Label(master,text="--", font='Montserrat 12')
stock_close.grid(column=1,row=7)

#STOCK VOLUME LABEL
stock_volume = Label(master, text="--",font='Montserrat 12')
stock_volume.grid(column=1, row=8)

#STOCK ADJ CLOSE LABEL
stock_adj_close = Label(master,text="--", font='Montserrat 12')
stock_adj_close.grid(column=1, row=9)

#STOCK SYMBOL USER INPUT/ENTRY
stock_symbol_input = Entry(master,width=12)
stock_symbol_input.grid(column=0,row=10,sticky="w")

#SUBMIT BUTTON
submit_button = Button(master,text='Search', width=5,command=findStock)
submit_button.grid(column=0,row=11, sticky="w")
  

label_stock_symbol = Label(master, text='Stock:',font='Montserrat 12')
label_stock_symbol.grid(column=0, row=2,sticky="w")

label_stock_date = Label(master, text='Date:',font='Montserrat 12')
label_stock_date.grid(column=0,row=3,sticky="w")

label_stock_open = Label(master, text='Open:',font='Montserrat 12')
label_stock_open.grid(column=0,row=4,sticky="w") 

label_stock_high = Label(master, text='High:',font='Montserrat 12')
label_stock_high.grid(column=0,row=5,sticky="w") 

label_stock_low = Label(master,text='Low:', font='Montserrat 12')
label_stock_low.grid(column=0,row=6,sticky="w") 

label_stock_close = Label(master,text='Close:', font='Montserrat 12')
label_stock_close.grid(column=0,row=7,sticky="w")

label_stock_volume = Label(master, text='Volume:',font='Montserrat 12') 
label_stock_volume.grid(column=0, row=8,sticky="w")

label_stock_adj = Label(master, text='Adj Close:',font='Montserrat 12')
label_stock_adj.grid(column=0,row=9,sticky="w")
 



v = Label(master, text="\n")
v.grid(column=0,row=10) 
  
master.mainloop() 