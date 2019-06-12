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

root = Tk()
root.title("STOCK-IT")
root.geometry("600x600")

top_frame = Frame(root, bg="red", width=300,height = 200, cursos="dot")
bottom_frame = Frame()

top_frame.pack(side = TOP)





root.mainloop()