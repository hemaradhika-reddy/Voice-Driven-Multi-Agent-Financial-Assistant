# data_ingestion/api_fetch.py
import yfinance as yf
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

class APIAgent:
    def __init__(self, alpha_vantage_key):
        self.ts = TimeSeries(key=alpha_vantage_key, output_format='pandas')
    
    def fetch_stock_data(self, symbol):
        stock = yf.Ticker(symbol)
        hist = stock.history(period="1d")
        return {
            "symbol": symbol,
            "price": hist["Close"].iloc[-1],
            "volume": hist["Volume"].iloc[-1]
        }

    def fetch_intraday(self, symbol):
        data, _ = self.ts.get_intraday(symbol=symbol, interval='5min')
        return data.to_dict()