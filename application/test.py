import yfinance as yf
import pandas as pd

# Fetching data for Reliance Industries (NSE)
tickers = yf.Tickers('RELIANCE.NS TCS.NS HDFCBANK.NS BHARTIARTL.NS')
data = tickers.history(period='1d')
live_data_json = data.to_json(orient='index')
print(live_data_json)


